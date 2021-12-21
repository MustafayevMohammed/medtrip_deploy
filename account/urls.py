from django.urls import path
from django.urls.base import reverse_lazy

from account.forms import  MyPasswordResetForm, NewPasswordForm
from .views import about_page, profile, register,loginPage,logout, registration_completed, registration_method
from django.contrib.auth import views as auth_views

app_name ='account'

urlpatterns = [
    path('register/',register,name='register'),
    path('registration_method/',registration_method,name = 'registration_method'),
    path('login/',loginPage,name='login'),
    path('profile/',profile,name = 'profile'),
    path('logout/',logout,name ='logout'),
    path('about/',about_page,name = 'about_page'),
    path('registration_completed/',registration_completed,name = 'registration_completed'),
    
    path('password_recovery/',
     auth_views.PasswordResetView.as_view(success_url = reverse_lazy('account:password_reset_done'),template_name="password_recovery.html",email_template_name = 'tokenuser.html',form_class= MyPasswordResetForm)
     ,name="password_recovery"),

    path('password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password-sent.html"), 
        name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('account:password_updated'),template_name="new_password.html",form_class= NewPasswordForm), 
     name="password_reset_confirm"),

    path('password_updated/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_updated.html"), 
        name="password_updated"),
]
