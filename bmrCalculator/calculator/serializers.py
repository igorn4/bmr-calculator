from rest_framework import serializers
from .models import UserProfile, DailyRegister

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class DailyRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRegister
        fields = '__all__'