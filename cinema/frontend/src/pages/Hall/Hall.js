import React, { Component } from 'react';
import Header from '../../components/Header/Header';

import './Hall.css';

class Hall extends Component {
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
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '179px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '202px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '226px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '250px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '274px',
                            top: '183px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '212px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '241px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '270px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '297px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '326px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '353px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '381px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '410px'
                        }}
                    />
                    <div
                        className="hall-seat"
                        style={{
                            left: '155px',
                            top: '440px'
                        }}
                    />
                </div>
            </div>
        );
    }
}

export default Hall;
