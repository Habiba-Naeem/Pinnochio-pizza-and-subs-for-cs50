from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from orders.models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs, Pastas, DinnerPlatters, Salads

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Product(models.Model):
    name = models.CharField( max_length = 20 )
    size =  models.CharField( max_length = 20 )
    toppings = models.CharField( max_length = 60 , null = True, blank = True)
    extras = models.CharField( max_length = 60 , null = True, blank = True)
    extra_price = models.DecimalField( max_digits = 10, decimal_places = 2 )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 )
    
    def __str__(self):
        return f"${self.price}, {self.name}, {self.size}, {self.toppings}, {self.extras}, {self.extra_price}"


class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        price = self.product.price * self.quantity
        return f"{self.product}, {self.quantity}, {price}"
