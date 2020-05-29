from django.db import models
# Create your models here.

Sizes = ( 
    ('Small', 'Small'),
    ('Large', 'Large')
)

No_of_Topping = (
    ('Cheese', 'Cheese'),
    ('One topping', '1 topping'),
    ('Two toppings', '2 toppings'),
    ('Three toppings', '3 toppings'),
    ('Five toppings', '5 toppings')
)

class Toppings(models.Model):
    topping =  models.CharField( max_length = 50 )

    def __str__(self):
        return f"{self.topping}"
"""
class Pizza(models.Model): 
    size = models.CharField( max_length = 50, choices = Sizes, default = Sizes )
    topping = models.CharField( max_length = 50, choices = No_of_Topping, default = No_of_Topping ) 
    def __str__(self):
        return f"{self.size}, {self.topping}"
"""
class Regular_Pizza(models.Model):
    size = models.CharField( max_length = 50, choices = Sizes)
    topping = models.CharField( max_length = 50, choices = No_of_Topping) 
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    
    def __str__(self):
        return f"${self.price}, {self.size}, {self.topping} "

class Sicilian_Pizza(models.Model):
    size = models.CharField( max_length = 50, choices = Sizes)
    topping = models.CharField( max_length = 50, choices = No_of_Topping) 
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    
    def __str__(self):
        return f"${self.price}, {self.size}, {self.topping} "

class Extra(models.Model):
    extra = models.CharField( max_length = 50, blank = True )
    price_of_extra = models.DecimalField( max_digits = 10, decimal_places = 2, null = True, blank = True) 
    
    def __str__(self):
        return f"{self.extra},  {self.price_of_extra}"

class Subs_Items(models.Model):
    sub = models.CharField( max_length = 50 )
    #extra = models.ForeignKey(Extra, on_delete=models.CASCADE, null = True, blank = True )
    
    def __str__(self):
        return f"{self.sub}"

class Subs(models.Model):
    size = models.CharField( max_length = 50, choices = Sizes, default = Sizes )
    subs_items = models.ForeignKey(Subs_Items, on_delete=models.CASCADE, null = True)
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    

    def __str__(self):
        return f"{self.subs_items}, ${self.price}, {self.size}"

class Pastas(models.Model):
    pasta = models.CharField( max_length = 50 )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    def __str__(self):
        return f"{self.pasta}, ${self.price}"

class Salads(models.Model):
    salad = models.CharField( max_length = 50 )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 ) 
    def __str__(self):
        return f"{self.salad}, ${self.price}"

class Platter_Item(models.Model):
    platter = models.CharField( max_length = 50,  null = True )
    def __str__(self):
        return f"{self.platter}"
    
class DinnerPlatters(models.Model):
    size = models.CharField( max_length = 50, choices = Sizes, default = Sizes )
    platter_item = models.ForeignKey(Platter_Item, on_delete=models.CASCADE, null = True )
    price = models.DecimalField( max_digits = 10, decimal_places = 2, null = True ) 

    def __str__(self):
        return f"{self.platter_item}, ${self.price}, {self.size},"
