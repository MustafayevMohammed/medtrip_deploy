from django.urls import path
from .views import about_page, profile, register,loginPage,logout, registration_completed, registration_method


app_name ='account'

urlpatterns = [
    path('register/',register,name='register'),
    path('registration_method/',registration_method,name = 'registration_method'),
    path('login/',loginPage,name='login'),
    path('profile/',profile,name = 'profile'),
    path('logout/',logout,name ='logout'),
    path('about/',about_page,name = 'about_page'),
    path('registration_completed/',registration_completed,name = 'registration_completed'),
    

]