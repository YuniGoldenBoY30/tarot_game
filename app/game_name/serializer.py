from rest_framework import serializers

from .models import *


class DescripcionNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescripcionNombres
        fields = '__all__'


class NombreDescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NombreDescripcion
        fields = '__all__'
