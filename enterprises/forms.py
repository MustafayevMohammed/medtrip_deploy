from django import forms
from django.db.models import fields
from . import models

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


