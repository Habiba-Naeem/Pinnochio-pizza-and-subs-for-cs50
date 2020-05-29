from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

# Create your views here
def index(request):
    if not request.user.is_authenticated:
        print("okay")
        return render(request, "user/index.html", {"message": None})
    context = {
        "user": request.user
    }
    return HttpResponseRedirect(reverse("cart") , context)

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("loogedin")
        return HttpResponseRedirect(reverse("index"))
    else:
        messages.warning(request, "Please provide correct username and password.")
        return HttpResponseRedirect(reverse("index"))
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password == confirm_password:
            try:
                if User.objects.get(username=username) or User.objects.get(email=email):
                    print("unscunceess")
                    messages.error(request, "Username or email already exists.")
                    return HttpResponseRedirect(reverse("register"))
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                messages.success(request, "Account created")
                user_log = authenticate(request, username=username, password=password)
                login(request, user_log)
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, "Passwords do not match")
            return HttpResponseRedirect(reverse("register"))
           
    return render(request, 'user/index.html')

   
"""
@login_required
def profile(request):
    return render(request, 'users/profile.html')"""


def cart(request):
    if not request.user.is_authenticated:
        print("okay")
        return HttpResponseRedirect(reverse('index'))
    return render(request, "user/cart.html")

