from rest_framework import serializers

from .models import *


class ConfiguracionTiradaserializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionTirada
        fields = '__all__'


class PaqueteCartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteCarta
        fields = '__all__'
