from rest_framework import serializers
from rest_framework.generics import ListAPIView
from enterprises.models import CategoryModel, CommentModel, CountryModel, DistrictModel, EnterpriseModel, ServiceModel, TourModel
from .serializers import CategorySeriliazer, CommentSeriliazer, CountrySeriliazer, DisctrictSeriliazer, EnterprisesSeriliazer, ServiceSeriliazer, TourSeriliazer

#----------------------------------------
class EnterprisesListApiView(ListAPIView):
    serializer_class = EnterprisesSeriliazer
    queryset = EnterpriseModel.objects.all()

#----------------------------------------
class CommentListApiView(ListAPIView):
    serializer_class = CommentSeriliazer
    queryset = CommentModel.objects.all()

#---------------------------------------
class ServiceListApiView(ListAPIView):
    serializer_class  = ServiceSeriliazer
    queryset  = ServiceModel.objects.all()
#---------------------------------------
class CategoryListApiView(ListAPIView):
    serializer_class = CategorySeriliazer
    queryset = CategoryModel.objects.all()
#---------------------------------------
class CountryListApiView(ListAPIView):
    serializer_class = CountrySeriliazer
    queryset = CountryModel
#---------------------------------------
class TourListApiView(ListAPIView):
    serializer_class = TourSeriliazer
    queryset = TourModel
#---------------------------------------
class DisctrictListApiView(ListAPIView):
    serializer_class = DisctrictSeriliazer
    queryset = DistrictModel