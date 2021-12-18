from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.forms.forms import Form
from django.contrib.auth.models import User
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from enterprises.models import CountryModel
from . models import CustomUserModel

class RegisterForm(UserCreationForm):

    email = forms.EmailField(label="Mail ünvaniniz",widget=forms.EmailInput(attrs={'class':'fields'}))
    first_name = forms.CharField(label="Adınız",widget=forms.TextInput(attrs={'class':'fields'}))
    last_name = forms.CharField(label="Soyadınız",widget=forms.TextInput(attrs={'class':'fields'}))

    country  = forms.ModelChoiceField(queryset=CountryModel.objects.all())
    phone = PhoneNumberField()
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class':'passfields','style':'text-align:center; margin-left:180px; width:65%; border-radius:3px;'})
    )
    password2 = forms.CharField(
        label="Parol Tesdiqle",
        widget=forms.PasswordInput(attrs={'class':'passfields','style':'text-align:center; margin-left:180px; width:65%; border-radius:3px;'})
    )

    class Meta:
        model = CustomUserModel
        fields = ["email","first_name","last_name","password1","password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'fields'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))