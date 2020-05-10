from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.decorators import login_required
#from django.contrib import messages
from .forms import Register

# Create your views here
def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "user/register.html", context)

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "user/login.html", {"message": "Please provide correct username and password."})


def logout_user(request):
    logout(request)
    return render(request, "user/login.html", {"message": "Logged out."})

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = Register()
    return render(request, 'user/register.html', {'form': form})

"""
@login_required
def profile(request):
    return render(request, 'users/profile.html')"""