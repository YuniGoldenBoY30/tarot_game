# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import *


class CategoriaBasicaView(viewsets.ModelViewSet):
    queryset = CategoriaBasica.objects.all()
    serializer_class = CategoriaBasicaSerializer


class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class NumeroView(viewsets.ModelViewSet):
    queryset = Numero.objects.all()
    serializer_class = NumeroSerializer


class CartaView(viewsets.ModelViewSet):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer


class DescripcionView(viewsets.ModelViewSet):
    queryset = Descripciones.objects.all()
    serializer_class = DescripcionSerializer


class TipoArcanoView(viewsets.ModelViewSet):
    queryset = TipoArcano.objects.all()
    serializer_class = TipoArcanoSerializer
