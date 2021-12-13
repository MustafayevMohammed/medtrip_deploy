from django.urls import path
from .views import CustomerListApiView, ProductCategoryListApiView, ItemListApiView, OrderItemListApiView,OrderListApiView

urlpatterns = [
    path('listcustomer/',CustomerListApiView.as_view(),name='customerlist'),
    path('listproductcategory/',ProductCategoryListApiView.as_view(),name='productcategorylist'),
    path('listitem/',ItemListApiView.as_view(),name='itemlist'),
    path('listorderitem/',OrderItemListApiView.as_view(),name='orderitemlist'),
    path('listorder/',OrderListApiView.as_view(),name='orderlist'),
]
