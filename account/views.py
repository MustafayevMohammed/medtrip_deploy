from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from . import forms
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.core.exceptions import ValidationError


# Create your views here.
@csrf_protect
def register(request):
    """form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            newUser= form.save(commit=False)
            newUser.save()
            return redirect("account:login")
    context = {
    "form":form
        }"""
    return render(request,"user_registration.html")

@csrf_protect
def loginPage(request):
    """form = forms.LoginForm()
    #if request.method == "POST":
        form = forms.LoginForm(request.POST)
        #email = request.POST.get("email")
        password = request.POST.get("password")
        
        account = authenticate(request,email=email,password=password)
        if account is None:
            raise ValidationError(request,"Emailiniz Ve Ya Parolunuz Sehvdir!")
        else:
            auth_login(request,account)
            return redirect("enterprises:mainpage")

    context = {
        "form":form
    }"""
    return render(request,"login.html")

def logout(request):
    #auth_logout(request)
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