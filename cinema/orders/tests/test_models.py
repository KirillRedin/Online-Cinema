from django.test import TestCase
from ..models import *


class GenreTest(TestCase):

    """ Test module for Genre model """

    def setUp(self):
        self.genre = Genre.objects.create(
            name = 'Жахи'
        )

    def test_genre(self):
        horror_genre = Genre.objects.get(id = self.genre.pk)
        self.assertEqual(horror_genre.name, 'Жахи')

class OrderTest(TestCase):
    """ Test module for Order model """

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
            name = 'Українська'
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
            email = 'john_doe@gmail.com',
            visitor_name = 'John Doe',
            status = 'locked',
            session_id = session.id,
            seat_id = seat.id
        )

    def test_order(self):
        first_order = Order.objects.get(id = self.order.id)
        self.assertEqual(
            first_order.visitor_name, 'John Doe'
        )