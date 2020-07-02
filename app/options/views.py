# Create your views here.
from rest_framework import viewsets

from .serializer import *


class ConfiguracionTiradaView(viewsets.ModelViewSet):
    queryset = ConfiguracionTirada.objects.all()
    serializer_class = ConfiguracionTiradaserializer


class PaqueteCartaView(viewsets.ModelViewSet):
    queryset = PaqueteCarta.objects.all()
    serializer_class = PaqueteCartaSerializer
