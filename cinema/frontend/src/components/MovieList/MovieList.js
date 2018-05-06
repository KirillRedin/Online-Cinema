import React, { Component } from 'react';
import Movie from '../Movie/Movie';

import './MovieList.css';

const movie1 = {
    name: 'Австралія',
    description: 'Сюжет фільму розповідає про долю головних героїв, захоплюючи зображення історичних ' +
    'подій (Друга Світова війна, зокрема, бомбування Дарвіна), а також соціальні проблеми (гендерні, ' +
    'расові відносини).',
    actors: ['Николь Кидман', 'Хью Джекман'],
    trailer: 'https://www.youtube.com/watch?v=mfI4hK9I2k0',
    genre: 'драма',
    duration: 165,
    release: 2008,
    poster: 'https://images-na.ssl-images-amazon.com/images/I/81tjCSbkc%2BL._SY445_.jpg',
    lang: 'укр'
};

const movie2 = {
    name: 'Бунтар Один. Зоряні Війни. Історія',
    description: 'Спеціально для Кирила.',
    actors: ['Фелісіті Джонс', 'Дієго Луна'],
    trailer: 'https://www.youtube.com/watch?v=x7i8Q5syCLw',
    genre: 'драма',
    duration: 133,
    release: 2016,
    poster: 'http://kino-na-xati.com/wp-content/uploads/2016/12/buntar-odyn-zoryani-vijny-istoriya.jpg',
    lang: 'укр'
};

class MovieList extends Component {
    render() {
        return (
            <div className="movie-list">
                <Movie
                    name={movie1.name}
                    description={movie1.description}
                    actors={movie1.actors}
                    trailer={movie1.trailer}
                    genre={movie1.genre}
                    duration={movie1.duration}
                    release={movie1.release}
                    poster={movie1.poster}
                    lang={movie1.lang}
                />
                <Movie
                    name={movie2.name}
                    description={movie2.description}
                    actors={movie2.actors}
                    trailer={movie2.trailer}
                    genre={movie2.genre}
                    duration={movie2.duration}
                    release={movie2.release}
                    poster={movie2.poster}
                    lang={movie2.lang}
                />
            </div>
        );
    }
}

export default MovieList;
