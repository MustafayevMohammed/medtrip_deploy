from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CountryModel)

admin.site.register(models.ServiceModel)

admin.site.register(models.CategoryModel)

admin.site.register(models.EnterpriseModel)

admin.site.register(models.CommentModel)

admin.site.register(models.DistrictModel)

admin.site.register(models.TourModel)