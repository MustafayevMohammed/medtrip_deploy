from django.contrib import admin

# Register your models here.
from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(Item)

admin.site.register(OrderItem)

admin.site.register(Order)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('email','phone_number')

admin.site.register(ProductCategory)