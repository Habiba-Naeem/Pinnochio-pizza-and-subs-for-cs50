function count(){
    var count = 0;
    document.querySelectorAll("#cart-item-total").forEach( t =>{
        count = parseFloat(t.dataset.total) + count;
    })
    total.textContent = "$" + count.toFixed(2);
    return count.toFixed(2);    
}


document.addEventListener('DOMContentLoaded', () => {
    var rows = document.querySelectorAll(".row");
    var cancel = document.querySelectorAll(".cancel");

    rows.forEach( row => {
        const prices = row.querySelector("#product-price");
        const extras = row.querySelectorAll("#product-extras");
        const quantity = row.querySelector("#cart-item-quantity");
        var total = row.querySelector("#cart-item-total");
        console.log(extras);

        if (extras.length > 0){
            var extra_price = 0;
            extras.forEach( extra =>{
                extra_price = 0.5 + extra_price;
            })

            total.textContent = "$" + ( (prices.dataset.price * quantity.dataset.quantity) + extra_price).toFixed(2);
            total.setAttribute("data-total", `${( (prices.dataset.price * quantity.dataset.quantity) + extra_price).toFixed(2)}`);
        }
        else{
            total.textContent = "$" +  (prices.dataset.price * quantity.dataset.quantity).toFixed(2);
            total.setAttribute("data-total", `${(prices.dataset.price * quantity.dataset.quantity).toFixed(2)}`);
        }
    })
    
    count();

    cancel.forEach( can =>{
        can.addEventListener("click", ()=>{
            const parent = can.parentNode.parentNode;
            const id = parent.id;
            console.log(id);

            var table = document.querySelector("#table");
            table.deleteRow(parent.rowIndex);
            count();

            const request = new XMLHttpRequest();
            request.open('GET', `/cart/cancel/${id}`, true);

            request.send();
            return false;
            
        })
    })

    //STRIPE
    var stripe = Stripe('pk_test_51GrotLFndG7VbPdRyG8LrsOsDLRCN8QrzhPKo0PLBew3Us0USJbjMuriQ3AD0p0CYgdvBgQdMe7gdCZ3wWBNaP6300ayLdsdxB');
    var elements = stripe.elements();
    
    var style = {
        base: {
          color: "#32325d",
        }
    };
          
    var card = elements.create("card", { style: style });
    card.mount("#card-element");
    
    card.on('change', function(event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
          displayError.textContent = event.error.message;
        } else {
          displayError.textContent = '';
        }
    });

    var form = document.getElementById('payment-form');


    const request = new XMLHttpRequest();
    request.open('GET', `/cart/secret/${String(count())}`, true);

    request.onload = () =>{
        const data = JSON.parse(request.responseText);
        var clientSecret = data.client_secret;

        // Call stripe.confirmCardPayment() with the client secret.
        form.addEventListener('submit', function(ev) {
            var confirmb = confirm(`You confirm to pay $${count()} for the selected items`);
            if ( confirmb === true ){
                ev.preventDefault();
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: data.context.user
                        }
                    }
                }).then(function(result) {
                    if (result.error) {
                        // Show error to your customer (e.g., insufficient funds)
                        console.log(result.error.message);
                    } 
                    else {
                        // The payment has been processed!
                        if (result.paymentIntent.status === 'succeeded') {
                            const request = new XMLHttpRequest();
                            request.open('GET', `/cart/order/${String(count())}`, true);
    
                            request.onload = () =>{
                                const data = JSON.parse(request.responseText);
                                console.log(data);
                                if(data.success){
                                    alert("Payment Successful");
                                }
                            }
                            request.send();
                            return false;
                        }
                    }
                });}
        })
    }
    request.send();
    return false;
   
})