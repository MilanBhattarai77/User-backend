from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()
    is_geo_enabled = serializers.ReadOnlyField()

    
    class Meta:
        model=UserInfo
        fields= '__all__'