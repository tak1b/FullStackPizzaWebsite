from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def menu(request):
    return HttpResponse("This is the menu page.")