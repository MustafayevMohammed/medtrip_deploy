from django.urls import path
from .views import CustomListApiView

urlpatterns = [
    path('listaccount/',CustomListApiView.as_view(),name = 'listaccount')
]
