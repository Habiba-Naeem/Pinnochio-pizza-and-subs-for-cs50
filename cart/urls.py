from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="cart"),
    path("cart_item/<item>", views.cart_item, name="cart_item")
]