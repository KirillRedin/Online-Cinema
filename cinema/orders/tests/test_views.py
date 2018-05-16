import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import *
from ..serializers import *


# initialize the APIClient app
client = Client()

class GetAllFilms(TestCase):
    """ Test module for GET all films API """

    def setUp(self):
        lang1 = Language.objects.create(
            name = 'Українська'
        )

        lang2 = Language.objects.create(
            name = 'Русский'
        )

        genre1 = Genre.objects.create(
            name = 'Жахи'
        )

        genre2 = Genre.objects.create(
            name = 'Триллер'
        )

        self.film1 = Film.objects.create(
            name = 'Воно',
            description = 'Опис фільму',
            language_id = lang1.id,
            subtitle_id = lang1.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre1.id
        )

        self.film2 = Film.objects.create(
            name = 'Молчание ягнят',
            description = 'Опис фільму',
            language_id = lang2.id,
            subtitle_id = lang1.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre2.id
        )

    def test_get_all_films(self):
        # get API response
        response = client.get(reverse('film_list'))
        # get data from db
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleFilmTest(TestCase):
    """ Test module for GET single film API """

    def setUp(self):
        lang1 = Language.objects.create(
            name = 'Українська'
        )

        lang2 = Language.objects.create(
            name = 'Русский'
        )

        genre1 = Genre.objects.create(
            name = 'Жахи'
        )

        genre2 = Genre.objects.create(
            name = 'Триллер'
        )

        self.film1 = Film.objects.create(
            name = 'Воно',
            description = 'Опис фільму',
            language_id = lang1.id,
            subtitle_id = lang1.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre1.id
        )

        self.film2 = Film.objects.create(
            name = 'Молчание ягнят',
            description = 'Опис фільму',
            language_id = lang2.id,
            subtitle_id = lang1.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre2.id
        )

    def test_get_valid_single_film(self):
        response = client.get(reverse('film_detail', kwargs={'id': self.film1.id}))
        film = Film.objects.get(id=self.film1.id)
        serializer = FilmSerializer(film)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_film(self):
        response = client.get(reverse('film_detail', kwargs={'id': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewFilmTest(TestCase):
    """ Test module for inserting a new film """

    def setUp(self):
        genre = Genre.objects.create(
            name='Жахи'
        )
        language = Language.objects.create(
            name='Українська'
        )
        self.valid_payload = {
            'name': 'new_name',
            'description': 'description',
            'language': language.id,
            'subtitle': language.id,
            'release_date': '2018-12-12',
            'duration': '12:12:12',
            'trailer': 'trailer',
            'actors': 'actors',
            'poster': 'poster',
            'genre': genre.id,

        }

    def test_create_valid_film(self):
        response = client.post(reverse('film_list'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateNewOrderTest(TestCase):
    """ Test module for inserting a new order """

    def setUp(self):
        hall = Hall.objects.create(
            name = 'hall_1'
        )

        seat_category = SeatCategory.objects.create(
            name = 'category1'
        )

        seat = Seat.objects.create(
            row = '1',
            number = '1',
            hall_id = hall.id,
            seat_category_id = seat_category.id
        )

        lang = Language.objects.create(
            name = 'Україньська'
        )

        genre = Genre.objects.create(
            name = 'Триллер'
        )

        film = Film.objects.create(
            name = 'Darkwood',
            description = 'description',
            language_id = lang.id,
            subtitle_id = lang.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre.id
        )

        session = Session.objects.create(
            start_time = '2017-10-10 20:00:00',
            hall_id = hall.id,
            film_id = film.id,
            format = "2D"
        )

        self.valid_payload = {
            'email': 'redinkirill.ua@gmail.com',
            'visitor_name': 'John Doe',
            'status': 'locked',
            'seat': seat.id,
            'session': session.id
        }

        self.invalid_payload = {
            'email': '',
            'visitor_name': 'John Doe',
            'status': 'locked',
            'seat_id': seat.id,
            'session_id': session.id
        }

    def test_create_valid_order(self):
        response = client.post(reverse('order_list'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_order(self):
        response = client.post(reverse('order_list'), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleOrderTest(TestCase):
    """ Test module for updating an existing order """

    def setUp(self):
        hall = Hall.objects.create(
            name = 'hall_1'
        )

        seat_category = SeatCategory.objects.create(
            name = 'category1'
        )

        seat = Seat.objects.create(
            row = '1',
            number = '1',
            hall_id = hall.id,
            seat_category_id = seat_category.id
        )

        lang = Language.objects.create(
            name = 'Україньська'
        )

        genre = Genre.objects.create(
            name = 'Триллер'
        )

        film = Film.objects.create(
            name = 'Darkwood',
            description = 'description',
            language_id = lang.id,
            subtitle_id = lang.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre.id
        )

        session = Session.objects.create(
            start_time = '2017-10-10 20:00:00',
            hall_id = hall.id,
            film_id = film.id,
            format = "2D"
        )

        self.order = Order.objects.create(
            email = 'redinkirill.ua@gmail.com',
            visitor_name = 'John Doe',
            status = 'locked',
            seat_id = seat.id,
            session_id = session.id
        )

        self.valid_payload = {
            'email': 'redinkirill.ua@gmail.com',
            'visitor_name': 'John Doe',
            'status': 'payed',
            'seat': seat.id,
            'session': session.id
        }

        self.invalid_payload = {
            'email': 'redinkirill.ua@gmail.com',
            'visitor_name': 'John Doe',
            'status': '',
            'seat': seat.id,
            'session': session.id
        }

    def test_valid_update_order(self):
        response = client.put(reverse('order_detail', kwargs={'id': self.order.id}), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_order(self):
        response = client.put(reverse('order_detail', kwargs={'id': self.order.id}), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleOrderTest(TestCase):
    """ Test module for deleting an existing order """
    def setUp(self):
        hall = Hall.objects.create(
            name = 'hall_1'
        )

        seat_category = SeatCategory.objects.create(
            name = 'category1'
        )

        seat = Seat.objects.create(
            row = '1',
            number = '1',
            hall_id = hall.id,
            seat_category_id = seat_category.id
        )

        lang = Language.objects.create(
            name = 'Україньська'
        )

        genre = Genre.objects.create(
            name = 'Триллер'
        )

        film = Film.objects.create(
            name = 'Darkwood',
            description = 'description',
            language_id = lang.id,
            subtitle_id = lang.id,
            release_date = '2018-05-06',
            duration = '01:20:20',
            trailer = 'trailer_link',
            actors = 'actors_list',
            poster = 'poster_link',
            genre_id = genre.id
        )

        session = Session.objects.create(
            start_time = '2017-10-10 20:00:00',
            hall_id = hall.id,
            film_id = film.id,
            format = "2D"
        )

        self.order = Order.objects.create(
            email = 'redinkirill.ua@gmail.com',
            visitor_name = 'John Doe',
            status = 'locked',
            seat_id = seat.id,
            session_id = session.id
        )

    def test_valid_delete_order(self):
        response = client.delete(reverse('order_detail', kwargs={'id': self.order.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_valid_delete_order(self):
        response = client.delete(reverse('order_detail', kwargs={'id': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
