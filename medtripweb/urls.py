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
    
    path('password_recovery/',
     auth_views.PasswordResetView.as_view(template_name="password_recovery.html"),
     name="password_recovery"),

    path('password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password-sent.html"), 
        name="password_sent"),

    path('new_password/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="new_password.html"), 
     name="new_password"),

    path('password_updated/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_updated.html"), 
        name="password_updated"),
]


