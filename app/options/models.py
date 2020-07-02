from django.conf import settings
from django.db import models


# Create your models here.

class ConfiguracionTirada(models.Model):
    configuracion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuraciones_tiradas'


class PaqueteCarta(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cover = models.FileField(upload_to=settings.MEDIA_CARTA, blank=True, null=True)
    relacion_barajas = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paquete_barajas'
