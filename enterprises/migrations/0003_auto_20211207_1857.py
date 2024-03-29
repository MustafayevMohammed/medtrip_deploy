# Generated by Django 3.2.4 on 2021-12-07 14:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0002_categorymodel_commentmodel_districtmodel_enterprisemodel_servicemodel_tourmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisemodel',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='enterprisemodel',
            name='authorized_person',
            field=models.CharField(max_length=100, null=True, verbose_name='Mesul sexs'),
        ),
        migrations.AddField(
            model_name='enterprisemodel',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
