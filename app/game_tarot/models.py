from django.conf import settings
from django.db import models


# Create your models here.

class CategoriaBasica(models.Model):
    categoria = models.CharField(max_length=255, blank=True, null=True)
    elemento = models.CharField(max_length=255, blank=True, null=True)
    valor_simbolico = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'categoria_basica'


class Color(models.Model):
    color = models.CharField(max_length=80, blank=True, null=True)
    valor_simbolico = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'color'


class Numero(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    significado = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'numero'


class Carta(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)
    imagen = models.FileField(upload_to=settings.MEDIA_CARTA, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria_basica = models.ForeignKey('CategoriaBasica', models.CASCADE, db_column='categoria_basica', blank=True,
                                         null=True)
    color = models.ForeignKey('Color', models.CASCADE, db_column='color', blank=True, null=True)
    numero = models.ForeignKey('Numero', models.CASCADE, db_column='numero', blank=True, null=True)
    tipo_arcano = models.ForeignKey('TipoArcano', models.CASCADE, db_column='tipo_arcano', blank=True, null=True)

    class Meta:
        db_table = 'carta'


class Descripciones(models.Model):
    id_carta = models.ForeignKey(Carta, models.CASCADE, db_column='id_carta', blank=True, null=True)
    posicion = models.BooleanField(blank=True, null=True)
    invertida = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'descripcion'


class TipoArcano(models.Model):
    tipo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tipo_arcano'
