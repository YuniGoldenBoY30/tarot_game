# Create your views here.
from rest_framework import viewsets

from .serializer import *


class DescripcionNombreView(viewsets.ModelViewSet):
    queryset = DescripcionNombres.objects.all()
    serializer_class = DescripcionNombreSerializer


class NombreDescripcionView(viewsets.ModelViewSet):
    queryset = NombreDescripcion.objects.all()
    serializer_class = NombreDescripcionSerializer
