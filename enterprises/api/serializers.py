from rest_framework import serializers
from enterprises.models import CategoryModel, CommentModel, CountryModel, DistrictModel, EnterpriseModel, ServiceModel, TourModel

class EnterprisesSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseModel
        fields=[
            'owner',
            'name',
            'authorized_person',
            'about',
            'number',
            'services',
            'category',
            'country',
            'address',
            'accepted'

        ]

class CommentSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            'count',
            'author',
            'content',
            'enterprise',
            'created',
            'rating'
        ]

#----------------------------------
class ServiceSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields  = [
            'name'
        ]
#-----------------------------------
class CategorySeriliazer(serializers.ModelSerializer):
    model = CategoryModel
    fields = ['name']

#-----------------------------------
class CountrySeriliazer(serializers.ModelSerializer):
    model = CountryModel
    fields = ['name'
    ]

#-----------------------------------
class TourSeriliazer(serializers.ModelSerializer):
    model = TourModel
    fields = [
        'name',
        'detail',
        'started_at',
        'where_tour_will_pass',
        'finished_at'
    ]
#-----------------------------------
class DisctrictSeriliazer(serializers.ModelSerializer):
    model = DistrictModel
    fields = ['name']

