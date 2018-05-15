import React from 'react';

import './HallSeat.css';

export default function HallSeat(props) {
    const style = {
        left: props.left + 'px',
        top: props.top + 'px'
    };
    return <div
        onClick={(e) => props.onClick(e)}
        className="hall-seat"
        style={
            (props.chosenPlace === props.id) ? { ...style, backgroundColor: 'rgb(223, 247, 250)', border: '1px solid rgb(96, 123, 136)' } : style
        }
    />;
}