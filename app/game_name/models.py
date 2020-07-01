from django.db import models


# Create your models here.
class NombreDescripcion(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'nombre_descripcion'


class DescripcionNombres(models.Model):
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'descripcion_nombres'
