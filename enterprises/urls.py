from django.urls.conf import include
from django.urls import path
from .views import *

app_name = 'enterprises'

urlpatterns = [
    path('',index,name='index'),
    path('sanatory',sanatory,name = 'sanatory'),
    path('tours',tours,name = 'tours'),
    path('detail/<str:id>/',detailpage,name ='detail'),
]