from rest_framework import serializers
from orders.models import Admin
from orders.models import CategoryPrice
from orders.models import Film
from orders.models import Genre
from orders.models import Hall
from orders.models import Language
from orders.models import Order
from orders.models import Seat
from orders.models import SeatCategory
from orders.models import Session


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = (
            'id',
            'name',
            'password'
        )


class CategoryPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPrice
        fields = (
            'seat_category_id',
            'session_id',
            'price'
        )


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
            'id',
            'name',
            'description',
            'language_id',
            'subtitle_id',
            'release_date',
            'duration',
            'trailer',
            'actors',
            'poster',
            'genre_id'
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name'
        )


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = (
            'id',
            'name',
            'seats_map'
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'name'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'email',
            'visitor_name',
            'status',
            'session_id',
            'seat_id',
            'locking_date'
        )


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'id',
            'row',
            'number',
            'hall_id',
            'seat_category_id',
        )


class SeatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'id',
            'name'
        )


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = (
            'id',
            'start_time',
            'hall_id',
            'film_id',
            'format'
        )