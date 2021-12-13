from market.models import *
from rest_framework import serializers
#---------------------------------------
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
#----------------------------------------
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
#---------------------------------------
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields ='__all__'
#----------------------------------------
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
#-----------------------------------------
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
