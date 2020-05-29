from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("<item>/<item_name>", views.items, name="items"),
    path("pizza/<item_name>", views.pizza, name="pizza"),
    path("pasta/<item_name>", views.pasta, name="pasta"),
    path("subs/<item_name>", views.subs, name="subs"),
    path("salad/<item_name>", views.salad, name="salad"),
    path("dinnerplatter/<item_name>", views.dinnerplatter, name="dinnerplatter"),
    path("price", views.price, name="price")
]
