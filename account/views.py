from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

from account.models import CustomUserModel
from market.models import Customer
from .forms import LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.core.exceptions import ValidationError


# Create your views here.
@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return HttpResponse('sizin hesabiniz var')
    else:
        if request.method == "POST":
            form  = RegisterForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                form.save()
                country = form.cleaned_data['country']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                user = CustomUserModel.objects.get(
                    email = email
                )
                customer = Customer.objects.create(
                    user=user,country = country,first_name = first_name ,last_name = last_name ,email=email,phone_number=phone_number
                    )
                customer.save()
                return redirect('/')
            else:
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render (request, 'user_registration.html',{'form':form})
        return render(request,"user_registration.html")

@csrf_protect
def loginPage(request):
    if request.user.is_authenticated:
        return HttpResponse('siz giris etmisiz')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user_data = authenticate(email=email,password=password)
                if user_data is None:
                    return HttpResponse('hesabiniz yoxdur')
                else:
                    auth_login(request,user_data)
                    return redirect('/')
            else:
                return HttpResponse('is valid deyil')

        return render(request,"login.html")

def logout(request):
    auth_logout(request)
    return redirect('account:login')

@csrf_protect
def about_page(request):
    return render(request,'about.html')



def registration_method(request):
    return render(request,'registration_method.html')

def profile(request):
    return render(request,'profile.html')
def registration_completed(request):
    return render(request,'registration_completed.html')