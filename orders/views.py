from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *

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


def pasta(request, item_name):
    print(Pastas.objects.get(pasta = item_name).price)
    context = {
        "item_name": item_name,
        "price": Pastas.objects.get(pasta = item_name).price
    }
    print("jooooooooooooooooo")
    return render(request, "orders/items.html", context)
    
def pizza(request, item_name):
    if item_name == "Regular Pizza":
        context = {
            "item_name": item_name,
            "pizza": True,
            "price": Regular_Pizza.objects.get(size = 'Small', topping = 'Cheese').price,
            "toppings": Toppings.objects.all()
        }
        print(Regular_Pizza.objects.all())
        return render(request, "orders/items.html", context)
    else:
        print(Sicilian_Pizza.objects.all())
        context = {
            "item_name": item_name,
            "pizza": True,
            "price": Sicilian_Pizza.objects.get(size = 'Small', topping = 'Cheese').price,
            "toppings": Toppings.objects.all()
        }
        return render(request, "orders/items.html", context)

def subs(request, item_name):
    try:
        print(Subs.objects.get(subs_items__sub = item_name, size = 'Small').price)
        context = {
            "item_name": item_name,
            "price": Subs.objects.get(subs_items__sub = item_name, size = 'Small').price,
            "subs": True,
            "extras": Extra.objects.all()
        }
    except Subs.DoesNotExist:
        context = {
            "item_name": item_name,
            "price": Subs.objects.get(subs_items__sub = item_name, size = 'Large').price,
            "subs": True,
            "extras": Extra.objects.all()
        }
        return render(request, "orders/items.html", context)
    return render(request, "orders/items.html", context)
    
def salad(request, item_name):
    print(Salads.objects.filter(salad = item_name))
    context = {
        "item_name": item_name,
        "price": Salads.objects.get(salad = item_name).price
    }
    return render(request, "orders/items.html", context)

def dinnerplatter(request, item_name):
    print(DinnerPlatters.objects.get(platter_item__platter = item_name, size = 'Small').price)
    context = {
        "item_name": item_name,
        "price": DinnerPlatters.objects.get(platter_item__platter = item_name, size = 'Small').price,
        "dinnerplatter": True
    }
    return render(request, "orders/items.html", context)
    

def price(request):
    context = {
        "pizzas" : Pizza.objects.all(),
        "no_of_toppings": dict(No_of_Topping),
        "pastas" : Pastas.objects.all(),
        "subs" : Subs.objects.all(),
        "dinnerplatters" : DinnerPlatters.objects.all(),
        "toppings" : Toppings.objects.all(),
        "salads" : Salads.objects.all(), 
        "regular": Regular_Pizza.objects.all(),
        "sicilian": Sicilian_Pizza.objects.all(),
        "extras": Extra.objects.all(),
        "sub_items": Subs_Items.objects.all()
    }
    return JsonResponse({"success":True})
   