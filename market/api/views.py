from rest_framework import serializers
from market.models import Customer, Item, Order, OrderItem, ProductCategory
from .serializers import CustomerSerializer, ItemSerializer, OrderItemSerializer, OrderSerializer, ProductCategorySerializer
from rest_framework.generics import ListAPIView

class CustomerListApiView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

#-------------------------------------
class ProductCategoryListApiView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
#-------------------------------------
class ItemListApiView(ListAPIView):
    serializer_class = ItemSerializer
    queryset  = Item.objects.all()
#-------------------------------------
class OrderItemListApiView(ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
#--------------------------------------
class OrderListApiView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()