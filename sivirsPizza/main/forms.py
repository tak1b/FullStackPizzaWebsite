from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from main.forms import *
from main.models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size",
                  "crust",
                  "sauce",
                  "cheese",
                  "toppings"
                  ]
        widgets = {
            'toppings': forms.CheckboxSelectMultiple()
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'address', 'cardNo', 'expMonth', 'expYear', 'cvv']