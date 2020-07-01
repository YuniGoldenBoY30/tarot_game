# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Carta(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    imagen = models.CharField(max_length=-1, blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    categoria_basica = models.ForeignKey('CategoriaBasica', models.DO_NOTHING, db_column='categoria_basica', blank=True, null=True)
    color = models.ForeignKey('Color', models.DO_NOTHING, db_column='color', blank=True, null=True)
    numero = models.ForeignKey('Numero', models.DO_NOTHING, db_column='numero', blank=True, null=True)
    tipo_arcano = models.ForeignKey('TipoArcano', models.DO_NOTHING, db_column='tipo_arcano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carta'


class CategoriaBasica(models.Model):
    categoria = models.CharField(max_length=-1, blank=True, null=True)
    elemento = models.CharField(max_length=-1, blank=True, null=True)
    valor_simbolico = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'categoria_basica'


class Color(models.Model):
    color = models.CharField(max_length=-1, blank=True, null=True)
    valor_simbolico = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class ConfiguracionTirada(models.Model):
    configuracion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracion_tirada'


class CorsheadersCorsmodel(models.Model):
    cors = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corsheaders_corsmodel'


class Descripcion(models.Model):
    id_carta = models.ForeignKey(Carta, models.DO_NOTHING, db_column='id_carta', blank=True, null=True)
    posicion = models.BooleanField(blank=True, null=True)
    invertida = models.BooleanField(blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descripcion'


class DescripcionNombres(models.Model):
    descripcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descripcion_nombres'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NombreDescripcion(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    sexo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.ForeignKey(DescripcionNombres, models.DO_NOTHING, db_column='descripcion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nombre_descripcion'


class Numero(models.Model):
    numero = models.CharField(max_length=-1, blank=True, null=True)
    significado = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numero'


class PaqueteCarta(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    cover = models.CharField(max_length=-1, blank=True, null=True)
    relacion_barajas = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paquete_carta'


class SignoCombNum(models.Model):
    signo = models.ForeignKey('SignoZodiaco', models.DO_NOTHING, db_column='signo', blank=True, null=True)
    num_calculado = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signo_comb_num'


class SignoZodiaco(models.Model):
    signo = models.CharField(max_length=-1, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signo_zodiaco'


class TipoArcano(models.Model):
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_arcano'
