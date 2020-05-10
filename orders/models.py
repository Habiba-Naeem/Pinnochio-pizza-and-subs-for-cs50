from django.db import models
# Create your models here.
Type_of_pizza = (
    ('Reg', 'Regular'),
    ('Sl', 'Sicilian')
)

Sizes = ( 
    ('S', 'Small'),
    ('L', 'Large')
)

No_of_Topping = (
    ('C', 'Cheese'),
    ('one', '1 topping'),
    ('two', '2 toppings'),
    ('three', '3 toppings'),
    ('five', '5 toppings')
)

class Toppings(models.Model):
    topping =  models.CharField( max_length = 20 )

    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model): 

    pizza = models.CharField( max_length = 20, choices = Type_of_pizza)
    size = models.CharField( max_length = 20, choices = Sizes )
    topping = models.CharField( max_length = 20, choices = No_of_Topping )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    
    def __str__(self):
        return f"{self.pizza} pizza,  {self.size}, {self.topping}, ${self.price}"

class Subs(models.Model):
    sub = models.CharField( max_length = 20 )
    size = models.CharField( max_length = 20, choices = Sizes )
    extras = models.CharField( max_length = 20, blank = True )
    price_of_extra = models.DecimalField( max_digits = 10, decimal_places = 2, null = True, blank = True) 
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    

    def __str__(self):
        return f"{self.sub},  {self.size}, ${self.price}"

class Pastas(models.Model):
    pasta = models.CharField( max_length = 20 )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    def __str__(self):
        return f"{self.pasta}, ${self.price}"

class Salads(models.Model):
    salad = models.CharField( max_length = 20 )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    def __str__(self):
        return f"{self.salad}, ${self.price}"

class DinnerPlatters(models.Model):
    platter = models.CharField( max_length = 20 )
    size = models.CharField( max_length = 20, choices = Sizes )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 

    def __str__(self):
        return f"{self.platter},  {self.size} , ${self.price}"