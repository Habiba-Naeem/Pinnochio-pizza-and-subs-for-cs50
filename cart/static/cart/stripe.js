document.addEventListener('DOMContentLoaded', () => {
    var total = document.querySelector("#total");
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
    var count = 0;
    document.querySelectorAll("#cart-item-total").forEach( t =>{
        count = parseFloat(t.dataset.total) + count;
    })
    total.textContent = "$" + count;
       

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
        
        var response = fetch('/cart/secret').then(function(response) {
            return response.json();}).then(function(responseJson) {

            var clientSecret = responseJson.client_secret;
            // Call stripe.confirmCardPayment() with the client secret.
            form.addEventListener('submit', function(ev) {
                ev.preventDefault();
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                    card: card,
                    billing_details: {
                        name: 'Jenny Rosen'
                    }
                    }
                }).then(function(result) {
                    if (result.error) {
                    // Show error to your customer (e.g., insufficient funds)
                    console.log(result.error.message);
                    } else {
                    // The payment has been processed!
                    if (result.paymentIntent.status === 'succeeded') {
                        // Show a success message to your customer
                        // There's a risk of the customer closing the window before callback
                        // execution. Set up a webhook or plugin to listen for the
                        // payment_intent.succeeded event that handles any business critical
                        // post-payment actions.
                    }
                    }
                });
                });
        });

       
})