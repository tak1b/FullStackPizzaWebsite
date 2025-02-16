from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
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
        return redirect("/")
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

@login_required(login_url='/login') 
def order(request):
    toppings = PizzaTopping.objects.all()

    if request.method == 'POST':
        form = PizzaForm(request.POST)

        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.save()  # Save pizza first (before ManyToMany field)

            form.save_m2m()  # 🔥 This ensures ManyToManyField (toppings) is saved

            # Store pizza ID in session for later delivery
            pending_pizza_ids = request.session.get('pending_pizza_ids', [])
            pending_pizza_ids.append(pizza.id)
            request.session['pending_pizza_ids'] = pending_pizza_ids

            # Redirect to continue shopping or checkout
            if 'add_another' in request.POST:
                return redirect('order')
            return redirect('delivery')
        else:
            return render(request, 'order.html', {'form': form, "toppings": toppings})

    else:
        form = PizzaForm()
        return render(request, 'order.html', {'form': form, "toppings": toppings})

@login_required(login_url='/login') 
def delivery_page(request):
    pizza_ids = request.session.get('pending_pizza_ids', [])
    if not pizza_ids:
        messages.error(request, "Please create a pizza order first")
        return redirect('order')

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.author = request.user
            delivery.save()
            
            # Associate all pending pizzas with this delivery
            for pizza_id in pizza_ids:
                pizza = Pizza.objects.get(id=pizza_id)
                pizza.delivery = delivery
                pizza.save()
            
            # Clear the session
            del request.session['pending_pizza_ids']
            
            messages.success(request, "Your pizza orders have been placed successfully!")
            return redirect('/confirmation')
    else:
        form = DeliveryForm()
    
    return render(request, 'delivery.html', {'form': form})

@login_required(login_url='/login') 
def my_orders(request):
    deliveries = Delivery.objects.filter(author=request.user).select_related('pizza')
    return render(request, 'my_orders.html', {'deliveries': deliveries})

def confirmation(request):
    orders   = Pizza.objects.all().filter(author=request.user)
    delivery = Delivery.objects.all().filter(author=request.user)
    
    return render(request, 'confirmation.html', {'orders' : orders, "delivery" : delivery})