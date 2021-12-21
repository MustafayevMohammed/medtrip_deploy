from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from . models import CustomUserModel
from django.contrib.auth.forms import PasswordResetForm

class NewPasswordForm(SetPasswordForm):
    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
class MyPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        """Ensure the email address exists in the system."""
        email = self.cleaned_data['email']
        return email.lower()
class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    country  = forms.CharField()
    phone_number = PhoneNumberField()
    password1 = forms.CharField()
    password2 = forms.CharField(
       
    )

    class Meta:
        model = CustomUserModel
        fields = ["phone_number","country","email","first_name","last_name","password1","password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'fields'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))




