from django.urls import path
from . import views

from .forms import RegisterForm

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name="logout"),
    path('order', views.order, name="order"),
    path('delivery/', views.delivery_page, name='delivery'),
    path('myorders/', views.my_orders, name='my_orders')
]