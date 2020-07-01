from django.db import models


# Create your models here.
class SignoZodiaco(models.Model):
    signo = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'signo_zodiaco'


class SignoCombNum(models.Model):
    signo = models.ForeignKey('SignoZodiaco', models.CASCADE, db_column='signo', blank=True, null=True)
    num_calculado = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'signo_comb_num'
