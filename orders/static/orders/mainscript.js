function linking(link, id){
    if(window.location.href !== "http://localhost:8000/"){
            link.href = `http://localhost:8000/${id}`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    var menu_section = document.querySelector("#menu");
    var menu_link = document.querySelector("#menu-link");
    var home_link = document.querySelector("#home-link");

    var login_article = document.querySelector("#login");
    var register_article = document.querySelector("#register");

    var top_reg_button = document.querySelector("#top-reg-button");
    var top_log_button = document.querySelector("#top-log-button");

    var login_button = document.querySelector("#login-button");
    var register_button = document.querySelector("#register-button");
    menu_link.addEventListener("click", ()=>{
        linking(menu_link, "#menu");
    })

    home_link.addEventListener("click", ()=>{
        linking(home_link, "#heading");
    })

    top_log_button.addEventListener("click", ()=>{
        if(login_article.style.display === "none"){
            login_article.style.display = "block";
            register_article.style.display = "none";
        }
        else{
            login_article.style.display = "none";
            register_article.style.display = "block";
        }
    })

    top_reg_button.addEventListener("click", ()=>{
        if(register_article.style.display === "none"){
            register_article.style.display = "block";
            login_article.style.display = "none";
        }
        else{
            register_article.style.display = "none";
            login_article.style.display = "block"
        }
    })
})