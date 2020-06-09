from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pizza/<item_name>", views.pizza, name="pizza"),
    path("pasta/<item_name>", views.pasta, name="pasta"),
    path("subs/<item_name>", views.subs, name="subs"),
    path("salad/<item_name>", views.salad, name="salad"),
    path("dinnerplatter/<item_name>", views.dinnerplatter, name="dinnerplatter"),
    path("price/<item_name>/<size>", views.price, name="price"),
    path("pizzaprice/<item_name>/<size>/<no_of_toppings>", views.pizza_price, name="pizzaprice")
]
