# Create your views here.
from rest_framework import viewsets

from .serializer import *


class SignoZodiacoView(viewsets.ModelViewSet):
    queryset = SignoZodiaco.objects.all()
    serializer_class = SignoZodiacoSerializer


class SignoCombNumView(viewsets.ModelViewSet):
    queryset = SignoCombNum.objects.all()
    serializer_class = SignoCobNumSerializer
