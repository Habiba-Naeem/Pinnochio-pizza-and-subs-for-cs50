from django.conf import settings
from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import json
import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def index(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to add to cart.")
        return HttpResponseRedirect(reverse("userindex"))

    context = {
        "user": request.user,
        "cart_items": Cart_Item.objects.filter(cart__user = request.user)
    }
    return render(request, "cart/cart.html", context)



def cart_item(request, item):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first to add to cart.")
        return JsonResponse({"success": False})

    stuff = json.loads(item)
    print(stuff)
    
    try:
        cart = Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user = request.user)
 
    add = Additional.objects.create()
   
    if stuff["toppings"] != "":
        toppings = []
        for top in stuff["toppings"]:
            toppings.append(Toppings.objects.get(topping = top))
            add.toppings.add(Toppings.objects.get(topping = top))

    if stuff["extra"] != "":
        extra = []
        for ext in stuff["extra"]:
            add.extra.add(Extra.objects.get(extra = ext))


    product = Product.objects.create(name = stuff["item_name"], size = stuff["size"], price = stuff["price"], category = Category.objects.get(menu__id = stuff["category"]), additional = add)
    cart_item = Cart_Item.objects.create(product = product, quantity = stuff["quantity"], cart = cart)
         
    return JsonResponse({"success": True})

def secret(request, amount):
    amount = float(amount)*100
    amount = int(amount)

    intent = stripe.PaymentIntent.create(
        amount= amount,
        currency='usd',

        # Verify your integration in this guide by including this parameter
        metadata={'integration_check': 'accept_a_payment'},
        )
    context = {
        "user": str(request.user)
    }
    return JsonResponse({"client_secret" : intent.client_secret,
                        "context":context})

def order(request, amount):

    cart = Cart.objects.get(user = request.user)
    cart_item = Cart_Item.objects.filter(cart = cart)

    for item in cart_item:
        order_items = Order_Items.objects.create(product = item.product, quantity = item.quantity, cart = item.cart)
        order = Order.objects.create(order_items = order_items, total = amount) 
        cart_item = Cart_Item.objects.get(id = item.id)
        cart_item.delete()

    return JsonResponse({"success": True})

def cancel(request, id):
    cart_item = Cart_Item.objects.get(id = id)
    cart_item.delete()

    return JsonResponse({"success": True})


def view_order(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first to add to cart.")
        return HttpResponseRedirect(reverse("index"))

    elif request.user.is_superuser:
        order = Order.objects.all()
        print(order)
        context = {
            "orders": Order.objects.all()
        }
        return render(request, "cart/order.html", context)