from django.urls import path
from . import views

from .forms import RegisterForm

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]