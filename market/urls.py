from django.urls import path
from . views import *

app_name = 'market'

urlpatterns = [

    path('cart/', cart, name="cart"),
    path('basket/',basket, name = 'basket'),
    path('order/',order,name = 'order'),
    path('add_cart/<str:id>/',add_cart,name ='add_cart'),
    path('remove_cart/<str:id>/',remove_cart,name ='remove_cart'),
    path('product/',product,name = 'product'),
    path('product_details/',product_details,name = 'product_details'),
    path('payment_method/',payment_method,name = 'payment_method')
]