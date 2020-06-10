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

stripe.api_key = 'sk_test_51GrotLFndG7VbPdRiDYCHdy2Svytuidnha5rzyr4b8aKp4Bqlxrp3LqrxX3Ihp91jCMUG3vbgayUk2qvIV5ziCsF00KbpgBfVP'



def index(request):
    if not request.user.is_authenticated:
        print("okay")
        return render(request, "user/index.html", {"message": None})
    cart_items = Cart_Item.objects.filter(cart__user = request.user)
    print(Cart_Item.objects.filter(cart__user = request.user))
    context = {
        "user": request.user,
        "cart_items": Cart_Item.objects.filter(cart__user = request.user)
    }
    return render(request, "cart/cart.html", context)


def cart_item(request, item):


    if not request.user.is_authenticated:
        print("okay")
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

    print(amount)
    amount = float(amount)*100
    print(amount)
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
    print(cart)
    cart_item = Cart_Item.objects.filter(cart = cart)
    print(cart_item)
    order_items = Order_Items.objects.create()

    for item in cart_item:
        print(item.id)
        order_items.cart_item.add(Cart_Item.objects.get(id= item.id))

    order = Order.objects.create(order_items = order_items, total = amount)
    print(order)
    return JsonResponse({"success": True})

