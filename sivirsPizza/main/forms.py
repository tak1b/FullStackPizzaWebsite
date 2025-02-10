from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label= ("Confirm Password"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
        help_texts = {
            'username': None,
            'email': None,
            'password1' : None,
            'password2' : None,
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size",
                  "crust",
                  "sauce",
                  "cheese",
                #   "pepporoni",
                #   "chicken",
                #   "ham",
                #   "pineapple",
                #   "mushrooms",
                #   "peppers",
                #   "onions",
                  ]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ["name",
                  "address",
                  "cardNo",
                  "expMonth",
                  "expYear",
                  "cvv"
                  ]