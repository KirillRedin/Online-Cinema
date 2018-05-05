import React, { Component } from 'react';
import DatePicker from 'material-ui/DatePicker/DatePicker';
import Header from '../../components/Header/Header';
import MovieList from '../../components/MovieList/MovieList';
import './Main.css';

class MainPage extends Component {
    render() {
        const in7Days = new Date();
        in7Days.setDate(in7Days.getDate() + 7);
        return (
            <div className="main-page">
                <Header/>
                <div className="other-info">
                    <DatePicker
                        container="inline"
                        hintText="Обрати іншу дату"
                        minDate={new Date()}
                        maxDate={in7Days}
                    />
                </div>
                <h2 className="main-page__header">Сьогодні в кінотеатрі</h2>
                <MovieList />
            </div>
        );
    }
}

export default MainPage;
