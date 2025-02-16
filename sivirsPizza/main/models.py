from django.db import models
from django.contrib.auth.models import User

######################## PIZZA CONFIG 

SIZE_CHOICES = (
    ("small", "small"),
    ("medium", "medium"),
    ("large", "large"),
)

CRUST_CHOICES = (
    ("thin", "thin"),
    ("normal", "normal"),
    ("thick", "thick"),
    ("gluten free", "gluten free"),
)

SAUCE_CHOICES = (
    ("tomato", "tomato"),
    ("vegan", "bbq"),
)

CHEESE_CHOICES = (
    ("mozzarella", "mozzarella"),
    ("vegan", "vegan"),
    ("low fat", "low fat"),
)

# Models to hold configuration items
class PizzaSize(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)

    def __str__(self):
        return self.crust

class PizzaCheese(models.Model):
    cheese = models.CharField(max_length=20)

    def __str__(self):
        return self.cheese

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return self.sauce

class PizzaTopping(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return self.topping

try:
    size_items = PizzaSize.objects.all()
    pizza_sizes = tuple((item.size, item.size) for item in size_items) or (('medium', 'medium'),)
except Exception:
    pizza_sizes = (('medium', 'medium'),)

try:
    crust_items = PizzaCrust.objects.all()
    pizza_crust_size = tuple((item.crust, item.crust) for item in crust_items) or (('normal', 'normal'),)
except Exception:
    pizza_crust_size = (('normal', 'normal'),)

try:
    sauce_items = PizzaSauce.objects.all()
    pizza_sauce = tuple((item.sauce, item.sauce) for item in sauce_items) or (('tomato', 'tomato'),)
except Exception:
    pizza_sauce = (('tomato', 'tomato'),)

try:
    cheese_items = PizzaCheese.objects.all()
    pizza_cheese = tuple((item.cheese, item.cheese) for item in cheese_items) or (('mozzarella', 'mozzarella'),)
except Exception:
    pizza_cheese = (('mozzarella', 'mozzarella'),)

######################## PIZZA MODEL

class Pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=pizza_sizes, default='medium')
    crust = models.CharField(max_length=20, choices=pizza_crust_size, default='normal')
    sauce = models.CharField(max_length=20, choices=pizza_sauce, default='tomato')
    cheese = models.CharField(max_length=20, choices=pizza_cheese, default='mozzarella')
    toppings = models.ManyToManyField(PizzaTopping)   
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Pizza by {self.author.username} on {self.date.strftime('%Y-%m-%d')}"

############# DELIVERY CONFIG

# Month choices for expiration date
MONTH_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

# Year choices for expiration date
YEAR_CHOICES = tuple((year, year) for year in range(2022, 2050))

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cardNo = models.IntegerField()
    expMonth = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    expYear = models.IntegerField(choices=YEAR_CHOICES, default=2000)
    cvv = models.IntegerField()

    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"
