from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cart_Item)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Additional)
admin.site.register(Order_Items)
admin.site.register(Order)