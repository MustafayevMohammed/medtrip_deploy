from typing import Match
from django.core import validators
from django.db import models
from django.db.models.expressions import F
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg

# Create your models here.

class DistrictModel(models.Model):
    name = models.CharField(max_length=120,verbose_name="Rayon Adi:")

    def __str__(self):
        return self.name

class CountryModel(models.Model):
    name = models.CharField(max_length=70,verbose_name="Olkenin adi:")
    flag = models.ImageField(upload_to="country_pictures",blank=False, null=False)

    def __str__(self):
        return self.name


class TourModel(models.Model):
    name = models.CharField(max_length=110,verbose_name="Turun adi:")
    detail = models.TextField(verbose_name="Turun detali:")
    started_at = models.ForeignKey(DistrictModel,related_name="tour_start",verbose_name="Baslangic bolgesi",on_delete=models.CASCADE)
    where_tour_will_pass = models.ManyToManyField(DistrictModel,related_name="tour_pass",verbose_name="Haralardan kececek:")
    finished_at = models.ForeignKey(DistrictModel,related_name="tour_fin",verbose_name="Bitis bolgesi",on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name
    



# ------------------------------------------------------------------------------------------

class ServiceModel(models.Model):
    name = models.CharField(max_length=120,blank=False, null=False,verbose_name="Xidmetin adi:")

    def __str__(self):
        return self.name

# ------------------------------------------------------------------------------------------


class CategoryModel(models.Model):
    name = models.CharField(max_length=150,verbose_name="Kategoriyanin adi",blank=False, null=False)

    def __str__(self):
        return self.name

# ------------------------------------------------------------------------------------------

class EnterpriseModel(models.Model):
    owner = models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,verbose_name = 'Sirket sahibi(email)',related_name='Sirketler',null=True,blank=False)
    name = models.CharField(max_length=150,verbose_name="Muessise adi")
    authorized_person = models.CharField(max_length=100,verbose_name='Mesul sexsin Adi',null=True,blank=False)
    about = models.TextField(verbose_name="Muessise haqqinda:",null=True,blank=True)
    number = PhoneNumberField(null=True,blank=False)
    services = models.CharField(max_length=100,null=True,blank=False)
    category = models.CharField(max_length=100,null=True,blank=False)
    country = models.CharField(verbose_name="Olke",max_length=100,null=True,blank=False)
    address = models.CharField(max_length=150,null=True,blank=True)
    
    def __str__(self):
        return self.name

    def averagereview(self):
        reviews = CommentModel.objects.filter(enterprise=self).aggregate(average=Avg("rating"))
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg
# ------------------------------------------------------------------------------------------


class CommentModel(models.Model):
    count = models.IntegerField(default=0)
    author = models.ForeignKey("account.CustomUserModel",related_name="comments",on_delete=models.CASCADE)
    content = models.CharField(max_length=1000,verbose_name="Commentin Mezmunu:")
    enterprise = models.ForeignKey(EnterpriseModel,related_name="comments",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.id)