from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

#-----------------------------------------------------------------------------------------
class Customer(models.Model):
    user = models.ForeignKey("account.CustomUserModel",on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20,verbose_name='phone number')

    def _str_(self):
        return self.username
#-------------------------------------------------------------------------------------------
class ProductCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name='kateqoriyalar')

    def _str_(self):
        return self.name
#------------------------------------------------------------------------------------------
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()

    def _str_(self):
        return self.title


    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(Customer,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def _str_(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    users = models.ForeignKey(Customer,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)