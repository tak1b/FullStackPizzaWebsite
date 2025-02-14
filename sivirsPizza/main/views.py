from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm  # Add this import
from django.contrib import messages

from main.forms import *
from django.contrib.auth.views import LoginView

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

class UserLoginForm(AuthenticationForm):  # Add this class
    pass

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect("/")

# @login_required(login_url='index') #redirect when user is not logged in
def order(request):
    toppings = PizzaTopping.objects.all()

    if request.method == 'POST':
        form = PizzaForm(request.POST)

        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.save()
            # Store pizza_id in session for delivery connection
            request.session['pending_pizza_id'] = pizza.id
            return redirect('/delivery')
        else:
            return render(request, 'order.html', {'form': form, "toppings": toppings})

    else:
        form = PizzaForm()
        return render(request, 'order.html', {'form': form, "toppings": toppings})

def delivery_page(request):
    # Check if there's a pending pizza order
    pizza_id = request.session.get('pending_pizza_id')
    if not pizza_id:
        messages.error(request, "Please create a pizza order first")
        return redirect('order')

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.author = request.user
            
            # Connect the pizza to this delivery
            pizza = Pizza.objects.get(id=pizza_id)
            delivery.pizza = pizza
            delivery.save()
            
            # Clear the pending pizza from session
            del request.session['pending_pizza_id']
            
            messages.success(request, "Your pizza order has been placed successfully!")
            return redirect('/')
    else:
        form = DeliveryForm()
    
    return render(request, 'delivery.html', {'form': form})

def my_orders(request):
    # Get all deliveries for the current user
    deliveries = Delivery.objects.filter(author=request.user).select_related('pizza')
    return render(request, 'my_orders.html', {'deliveries': deliveries})
