from rest_framework import serializers

from .models import *


class CategoriaBasicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaBasica
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numero
        fields = '__all__'


class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'


class DescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descripciones
        fields = '__all__'


class TipoArcanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoArcano
        fields = '__all__'
