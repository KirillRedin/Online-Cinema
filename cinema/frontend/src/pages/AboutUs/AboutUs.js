import React, { Component } from 'react';
import Header from '../../components/Header/Header';

class Login extends Component {
    render() {
        return (
            <div>
                <Header />
                <div style={{
                    position: 'fixed',
                    width: '100%',
                    height: '100%',
                    padding: '90px 5%',
                    display: 'flex',
                    backgroundColor: '#222'
                }}>
                    <div>
                        <img
                            src={"/static/us.jpg"}
                            alt="Це ми"
                            style={{
                                width: '600px',
                                marginRight: '15px'
                            }}
                        />
                    </div>
                    <div style={{marginTop: '15px', fontSize: '23px', color: '#DFF7FA'}}>Ми дуже класна команда</div>
                </div>
            </div>
        );
    }
}

export default Login;
