from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('enterprises.urls')),
    path("user/",include("account.urls")),
    path("market/",include("market.urls")),
    path('api/enterprises/',include('enterprises.api.urls')),
    path('api/market/',include('market.api.urls')),
    path('api/account/',include('account.api.urls')),
    
]

