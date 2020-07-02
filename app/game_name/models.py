from django.db import models


# Create your models here.
class DescripcionNombres(models.Model):
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'descripcion_nombres'


class NombreDescripcion(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.ForeignKey('DescripcionNombres', models.CASCADE, db_column='descripion', blank=True, null=True)

    class Meta:
        db_table = 'nombre_descripcion'
