from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def menu(request):
    return render(request, 'menu.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/register")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})


def login(response):
    return render(response, "login.html")
