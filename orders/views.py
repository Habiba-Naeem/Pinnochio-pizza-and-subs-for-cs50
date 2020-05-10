from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "pizzas" : Pizza.objects.all(),
        "pastas" : Pastas.objects.all(),
        "subs" : Subs.objects.all(),
        "dinner-pallets" : DinnerPlatters.objects.all(),
        "toppings" : Toppings.objects.all(),
        "salads" : Salads.objects.all()
    }
    return render(request, "orders/index.html", context)


