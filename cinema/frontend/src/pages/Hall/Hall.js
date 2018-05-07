import React, { Component } from 'react';
import RaisedButton from 'material-ui/RaisedButton/RaisedButton';
import Header from '../../components/Header/Header';
import HallSeat from '../../components/HallSeat/HallSeat';
import {Link} from 'react-router-dom';

import './Hall.css';

class Hall extends Component {
    constructor(props) {
        super(props);
        this.state = {
            chosenPlace: '',
            chosenRow: '',
            chosenSeat: '',
        };
    }

    renderHallSeats = () => {
        const returnedArray = [];
        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 21; j++) {
                const id = `${i+1}/${j+1}`;
                returnedArray.push(
                    <HallSeat
                        id={id}
                        key={id}
                        chosenPlace={this.state.chosenPlace}
                        left={155 + j*23.7}
                        top={183 + i*28.6}
                        onClick={(e) => this.chosePlace(e, i, j) }
                    />
                )
            }
        }
        return returnedArray;
    };

    chosePlace = (e, row, seat) => {
        const chosenPlace = `${row+1}/${seat+1}`;
        if (chosenPlace === this.state.chosenPlace) {
            this.setState({chosenPlace: '', chosenRow: '', chosenSeat: {}});
            return;
        }
        this.setState({
            chosenPlace: chosenPlace,
            chosenRow: row + 1,
            chosenSeat: seat + 1
        });
    };

    render() {
        return (
            <div>
                <Header />
                <div style={{
                    overflow: 'auto',
                    textAlign: 'center',
                    position: 'relative',
                    backgroundImage: 'url("/static/hall.png")',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat',
                    height: '500px',
                    width: '795px',
                    margin: 'auto',
                    backgroundSize: 'contain'
                }}>
                    {this.renderHallSeats()}
                </div>
                {
                    this.state.chosenPlace &&
                    <div style={{ textAlign: 'center' }}>
                        <div>Обране місце: {this.state.chosenPlace}</div>
                        <div>
                            <RaisedButton
                                label="Забронювати"
                                style={{marginTop: '10px', marginRight: '10px'}}
                                containerElement={<Link to={`/book/0/${21*(this.state.chosenRow-1) + this.state.chosenSeat}`} />}
                            />
                            <RaisedButton
                                label="Сплатити"
                                style={{marginTop: '10px'}}
                                containerElement={<Link to={`/book/1/${21*(this.state.chosenRow-1) + +this.state.chosenSeat}`} />}
                            />
                        </div>
                    </div>
                }
            </div>
        );
    }
}

export default Hall;
