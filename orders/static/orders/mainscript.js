function linking(link, id){
    if(window.location.href !== "http://localhost:8000/"){
            link.href = `http://localhost:8000/${id}`;
    }
}
/*function addtocart(select, no_of_topping_select, topping, size){
    var pizza_type = select.options[select.selectedIndex].value;
    var pizza_no_of_topping = no_of_topping_select.options[no_of_topping_select.selectedIndex].value;
    var top = () =>{
        for (var i = 0; i < topping.length; i++) {
            top.push(topping[i].value)
          }
    };
    var size = 
        
};*/
/*
function loadprice(item){
    let selection = document.querySelector(`#pizza #select-type`);
    let topping = document.querySelector(`#pizza #select-no-of-top`);
    let size = document.querySelector(`#pizza .size:checked`);

    console.log(selection);
    console.log(topping);
    console.log(size);

    const request = new XMLHttpRequest();
    request.open('GET', 'price', true);

    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.context){
            console.log(data);
        }
        else{
            console.log("unsucees");
        }
    }
    const data = {
        selection: selection,
        topping: topping,
        size: size
    }
    request.send(data);
    return false;
}
*/
document.addEventListener('DOMContentLoaded', () => {
    var menu_section = document.querySelector("#menu");
    var menu_link = document.querySelector("#menu-link");
    var home_link = document.querySelector("#home-link");

    var login_button = document.querySelector("#login-button");
    var register_button = document.querySelector("#register-button");

    var pizza = document.querySelector("#pizza");
    var items_buttons = document.querySelectorAll(".items");

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
    //loadprice(pizza);

    
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

    

    /*add_to_cart_button_regular_pizza.addEventListener("click", ()=>{
        var pizza_type_select = document.querySelector("#allpizza .pizza-select");
        var no_of_topping_select = document.querySelector("#allpizza #pizza-select-no-of-top");
        var toppings = document.querySelectorAll("#allpizza .toppings:checked");
        var size = document.querySelector("#allpizza input[name = 'size']:checked");
        addtocart(pizza_type_select, no_of_topping_select, toppings, size);
    })*/
})