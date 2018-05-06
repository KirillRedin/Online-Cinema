import React, { Component } from 'react';
import {Link} from 'react-router-dom';

import './Movie.css';

// test movie
class Movie extends Component {
    render() {
        const { description, name, actors, trailer, genre, duration, release, poster, lang } = this.props;
        return (
            <div className="movie">
                <div className="movie-poster">
                    <img src={poster} alt={name} />
                </div>
                <div className="movie-info">
                    <div className="movie-info__name">{name}</div>
                    <div>
                        Сюжет: <span>{description}</span>
                    </div>
                    <div>
                        В ролях: <span>{actors.join(', ')}</span>
                    </div>
                    <div>
                        Жанр: {genre}
                    </div>
                    <div>
                        Трейлер: <a href={trailer} target="_blank">тут</a>
                    </div>
                    <div>
                        Тривалість: {duration}хв
                    </div>
                    <div>
                        Дата виходу: {release}
                    </div>
                    <div>
                        Мова: {lang}
                    </div>
                    <div>
                        Субтитри: -
                    </div>
                    <div>
                        Час: <Link to="/hall">14:00</Link>, <Link to="/hall">18:00</Link>, <Link to="/hall">22:00</Link>
                    </div>
                </div>
            </div>
        );
    }
}

export default Movie;
