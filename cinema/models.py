# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class CategoryPrice(models.Model):
    seat_category = models.ForeignKey('SeatCategory', models.DO_NOTHING, primary_key=True)
    session = models.ForeignKey('Session', models.DO_NOTHING)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'category_price'
        unique_together = (('seat_category', 'session'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Film(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    subtitle = models.ForeignKey('Language', models.DO_NOTHING, blank=True, null=True)
    release_date = models.DateField()
    duration = models.TimeField(blank=True, null=True)
    trailer = models.CharField(max_length=255, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'film'


class Genre(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'genre'


class Hall(models.Model):
    name = models.CharField(max_length=45)
    seats_map = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hall'


class Language(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'language'


class Order(models.Model):
    email = models.CharField(max_length=45)
    visitor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=45)
    session = models.ForeignKey('Session', models.DO_NOTHING)
    seat = models.ForeignKey('Seat', models.DO_NOTHING)
    locking_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order'


class Seat(models.Model):
    row = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    hall = models.ForeignKey(Hall, models.DO_NOTHING)
    seat_category = models.ForeignKey('SeatCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seat'


class SeatCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'seat_category'


class Session(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    hall = models.ForeignKey(Hall, models.DO_NOTHING)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    format = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'
