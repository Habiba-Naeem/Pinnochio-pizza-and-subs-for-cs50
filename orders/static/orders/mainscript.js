document.addEventListener('DOMContentLoaded', () => {
    var topping_type_option = document.querySelector(".pizza-select");
    var topping = document.querySelector(".pizza-select-toppings");
    
    if (topping_type_option.options[0].value === 'Cheese'){
        topping.disabled = "true";
    }
})