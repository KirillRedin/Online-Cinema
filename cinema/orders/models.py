from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'admin'



class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'genre'


class Hall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    seats_map = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'hall'


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'language'



class Film(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, related_name='language_id')
    subtitle = models.ForeignKey('Language', models.DO_NOTHING, related_name='subtitle_id', blank=True, null=True)
    release_date = models.DateField()
    duration = models.TimeField(blank=True, null=True)
    trailer = models.CharField(max_length=255, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        db_table = 'film'


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    row = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    hall = models.ForeignKey('Hall', models.DO_NOTHING)
    seat_category = models.ForeignKey('SeatCategory', models.DO_NOTHING)

    class Meta:
        db_table = 'seat'


class SeatCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'seat_category'


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    hall = models.ForeignKey('Hall', models.DO_NOTHING)
    film = models.ForeignKey('Film', models.DO_NOTHING)
    format = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'session'


class CategoryPrice(models.Model):
    id = models.AutoField(primary_key=True)
    seat_category = models.ForeignKey('SeatCategory', models.DO_NOTHING, related_name='seat_category_id')
    session = models.ForeignKey('Session', models.DO_NOTHING, related_name='session_id')
    price = models.FloatField()

    class Meta:
        db_table = 'category_price'
        unique_together = (('seat_category', 'session'),)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    visitor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=45)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    locking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'
