from django.contrib import admin

# Register your models here.
from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(Item)

admin.site.register(OrderItem)

admin.site.register(Order)

admin.site.register(Customer)

admin.site.register(ProductCategory)