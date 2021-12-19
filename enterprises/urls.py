from django.urls.conf import include
from django.urls import path
from .views import *

app_name = 'enterprises'

urlpatterns = [
    path('',index,name='index'),
    path('sanatory',sanatory,name = 'sanatory'),
    path('detail/',detailpage,name = 'detail'),
    path('company_registration',company_registration,name ='company_registration')
]