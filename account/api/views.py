from rest_framework import serializers

from account.models import CustomUserModel
from .serializers import CustomSerializer
from rest_framework.generics import ListAPIView

class CustomListApiView(ListAPIView):
    serializer_class = CustomSerializer
    queryset = CustomUserModel.objects.all()