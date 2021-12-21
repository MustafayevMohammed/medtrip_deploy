from django import forms
from django.db.models import fields
from . import models

class CommentForm(forms.ModelForm):
    
    class Meta:

        model = models.CommentModel
        fields = ["content","rating"]


class EnterpriseRegisterForm(forms.ModelForm):
   

    class Meta:
        model = models.EnterpriseModel

        fields = ["name","authorized_person","number","category","country"]

