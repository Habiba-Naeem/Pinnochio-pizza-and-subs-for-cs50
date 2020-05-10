from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here
def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/index.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "user/index.html", context)

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "user/index.html", {"message": "Please provide correct username and password."})


def logout_user(request):
    logout(request)
    return render(request, "user/index.html", {"message": "Logged out."})

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        
        check_user = authenticate( username = username, email = email)

        if check_user is None:

            if password == confirm_password:
            
                user = User.objects.create_user( username = username, first_name = first_name, last_name = last_name, email = email, password = password)
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
            
            else:
                return render(request, 'user/index.html', {'message': "Provide matching password"})
        
        else:
            return render(request, 'user/index.html', {'message': "User already exists"})

    return render(request, 'user/index.html')

"""
@login_required
def profile(request):
    return render(request, 'users/profile.html')"""