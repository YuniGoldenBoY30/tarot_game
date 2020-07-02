from rest_framework import serializers

from .models import *


class SignoZodiacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignoZodiaco
        fields = '__all__'


class SignoCobNum(serializers.ModelSerializer):
    class Meta:
        model = SignoCombNum
        fields = '__all__'
