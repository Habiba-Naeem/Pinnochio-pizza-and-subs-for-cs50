function linking(link, id){
    if(window.location.href !== "http://localhost:8000/"){
            link.href = `http://localhost:8000/${id}`;
    }
}

function load_pizza_price(item_name, size, no_of_toppings){
    
    const request = new XMLHttpRequest();
    request.open('GET', `/pizzaprice/${item_name}/${size}/${no_of_toppings}`, true);

    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data){
            console.log(data);
            price.textContent = "$" + data["context"]["price"];
            price.dataset.price = data["context"]["price"];
        }
        else{
            console.log("unsucees");
        }
    }
    request.send();
    return false;
}


function loadprice(item_name, size){
    const request = new XMLHttpRequest();
    request.open('GET', `/price/${item_name}/${size}`, true);

    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data){
            console.log(data);
            price.textContent = "$" + data["context"]["price"];
            price.dataset.price = data["context"]["price"];
        }
        else{
            console.log("unsucees");
        }
    }
    request.send();
    return false;
}



document.addEventListener('DOMContentLoaded', () => {
    var menu_section = document.querySelector("#menu");
    var menu_link = document.querySelector("#menu-link");
    var home_link = document.querySelector("#home-link");

    var login_button = document.querySelector("#login-button");
    var register_button = document.querySelector("#register-button");
    var add_to_cart =  document.querySelector("#add-to-cart");
    
    var items_buttons = document.querySelectorAll(".items");

    var size = document.querySelectorAll(".size");
    var no_of_toppings  =  document.querySelectorAll(".no-of-toppings");
    var quantity = document.querySelector("#quantity");
   

    items_buttons.forEach( items_button => {
        items_button.addEventListener("click", () => {
            const parent = items_button.parentNode.parentNode.id;
            console.log(parent);

            const request = new XMLHttpRequest();
            request.open('GET', `${parent}`);
            request.onload = () =>{
                window.location.href = `http://127.0.0.1:8000/${parent}/${items_button.textContent}`;
            }
            request.send();
            return false;
        })
    });

    size.forEach( s => {
        s.addEventListener("change", () => {
            const new_size = document.querySelector(".size:checked").value;
            const item_name = document.querySelector("#itemname").textContent;
            quantity.value = 1;
            if (item_name === "Regular Pizza" || item_name === "Sicilian Pizza"){
                const no_of_toppings = document.querySelector(".no-of-toppings:checked").value;
                load_pizza_price(item_name, new_size, no_of_toppings);
            }
            else{
                loadprice(item_name, new_size);
            }
            
        })
    })

    no_of_toppings.forEach( t => {
        t.addEventListener("change", () => {
            const new_size = document.querySelector(".size:checked").value;
            const no_of_toppings = document.querySelector(".no-of-toppings:checked").value;
            const item_name = document.querySelector("#itemname").textContent;
            const quantity = document.querySelector("#quantity");
            quantity.value = 1;
            load_pizza_price(item_name, new_size, no_of_toppings);
        })
    })

    quantity.addEventListener("change", ()=>{
        const price = document.querySelector("#price");
        price.textContent = "$" + (price.dataset.price * quantity.value).toFixed(2);
    })
    
    /*for( let i = 0 ; i < toppings.length ; i++){
        toppings[i].onclick = selectiveCheck;
        function selectiveCheck (event) {
        var checked = document.querySelectorAll(".toppings:checked");
        if (checked.length > 3)
            return false;
        }
    }*/
    menu_link.addEventListener("click", ()=>{
        linking(menu_link, "#menu");
    })

    home_link.addEventListener("click", ()=>{
        linking(home_link, "#heading");
    })

    add_to_cart.addEventListener("click", ()=>{
        var tops = [];
        var ex = [];
        document.querySelectorAll(".toppings:checked").forEach( t =>{
            tops.push(t.value);
        })
        document.querySelectorAll(".extra:checked").forEach( e =>{
            ex.push(e.value);
        })
        
        const item = {
            "item_name": document.querySelector("#itemname").textContent,
            "category": document.querySelector("#itemname").dataset.category,
            "quantity" : document.querySelector("#quantity").value,
            "price" : document.querySelector("#price").dataset.price,
            "size" : document.querySelector(".size:checked").value,
            "toppings" : tops,
            "extra" : ex
       }
        const convert = JSON.stringify(item);
       
        const request = new XMLHttpRequest();
        request.open('GET', `/cart/cart_item/${convert}`, true);

        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success){
                console.log("okay")
            }
            else{
                console.log("not okay")
            }
        }
        request.send();
        return false;
    })

    cancel.forEach( can=>{
        can.addEventListener("click", ()=>{

        })
    })    

})