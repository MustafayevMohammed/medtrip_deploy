from django import forms
from django.db.models import fields
from phonenumber_field.modelfields import PhoneNumberField
from . import models

from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.ModelForm):
    
    class Meta:
        widgets = {
            "content" : forms.Textarea(attrs={"class":"fields",
            "cols":81,
            "rows":6,
            "style":"resize:none;"}),
        }
        model = models.CommentModel
        fields = ["content","rating"]


class EnterpriseRegisterForm(forms.ModelForm):
   
    accept_terms = forms.BooleanField()

    class Meta:
        model = models.EnterpriseModel

        fields = ["name","authorized_person","number","services","category","country","address","accept_terms"]


class AdviceForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    textarea = forms.CharField(max_length=1000)
    def __str__(self):
        return self.email