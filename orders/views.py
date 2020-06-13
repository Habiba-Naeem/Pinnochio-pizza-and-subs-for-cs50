from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from cart.models import Category


# Create your views here.
def index(request):
    context = {
        "no_of_toppings": dict(No_of_Topping),
        "pastas" : Pastas.objects.all(),
        "subs" : Subs.objects.all(),
        "dinnerplatters" : DinnerPlatters.objects.all(),
        "toppings" : Toppings.objects.all(),
        "salads" : Salads.objects.all(), 
        "regular": Regular_Pizza.objects.all(),
        "sicilian": Sicilian_Pizza.objects.all(),
        "extras": Extra.objects.all(),
        "sub_items": Subs_Items.objects.all(),
        "platter_items": Platter_Item.objects.all()
    }
    return render(request, "orders/index.html", context)


#return each menu item based on selection of the user
def pasta(request, item_name):
    context = {
        "item_name": item_name,
        "category": Category.objects.get(menu__menu = "Pasta").id,
        "price": Pastas.objects.get(pasta = item_name).price
    }
    return render(request, "orders/items.html", context)
    
def pizza(request, item_name):
    if item_name == "Regular Pizza":
        context = {
            "item_name": item_name,
            "category": Category.objects.get(menu__menu = "Regular Pizza").id,
            "pizza": True,
            "price": Regular_Pizza.objects.get(size = 'Small', topping = 'Cheese').price,
            "toppings": Toppings.objects.all()
        }
        return render(request, "orders/items.html", context)

    else:
        context = {
            "item_name": item_name,
            "category": Category.objects.get(menu__menu = "Sicilian Pizza").id,
            "pizza": True,
            "price": Sicilian_Pizza.objects.get(size = 'Small', topping = 'Cheese').price,
            "toppings": Toppings.objects.all()
        }
        return render(request, "orders/items.html", context)



def subs(request, item_name):
    try:
        context = {
            "item_name": item_name,
            "price": Subs.objects.get(subs_items__sub = item_name, size = 'Small').price,
            "subs": True,
            "category": Category.objects.get(menu__menu = "Subs").id,
            "extras": Extra.objects.all()
        }
    #if subs with small size do not exists
    except Subs.DoesNotExist:
        context = {
            "item_name": item_name,
            "price": Subs.objects.get(subs_items__sub = item_name, size = 'Large').price,
            "subs": True,
            "category":Category.objects.get(menu__menu = "Subs").id,
            "extras": Extra.objects.all()
        }
        return render(request, "orders/items.html", context)

    return render(request, "orders/items.html", context)
    
def salad(request, item_name):
    print(Salads.objects.filter(salad = item_name))
    context = {
        "item_name": item_name,
        "category": Category.objects.get(menu__menu = "Salad").id,
        "price": Salads.objects.get(salad = item_name).price
    }
    return render(request, "orders/items.html", context)

def dinnerplatter(request, item_name):
    context = {
        "item_name": item_name,
        "category": Category.objects.get(menu__menu = "Dinner Platter").id,
        "price": DinnerPlatters.objects.get(platter_item__platter = item_name, size = 'Small').price,
        "dinnerplatter": True
    }
    return render(request, "orders/items.html", context)


#displaying the price 
def price(request, item_name, size):
    try:
        print(Subs.objects.get(subs_items__sub = item_name, size = size).price)
        context = {
            "price": Subs.objects.get(subs_items__sub = item_name, size = size).price
        }
    except Subs.DoesNotExist:
        context = {
            "price": DinnerPlatters.objects.get(platter_item__platter = item_name, size = size).price
        }
    return JsonResponse({"context": context})
    
def pizza_price(request, item_name, size,  no_of_toppings):
    if item_name == "Regular Pizza":
        context = {
            "price": Regular_Pizza.objects.get(size = size, topping = no_of_toppings).price
        }
    else:
        context = {
            "price": Sicilian_Pizza.objects.get(size = size, topping = no_of_toppings).price
        }
    return JsonResponse({"context": context})
   