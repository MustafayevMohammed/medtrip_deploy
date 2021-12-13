from rest_framework import serializers
from account.models import CustomUserModel

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'