import React, { Component } from 'react';
import TextField from 'material-ui/TextField/TextField';
import RaisedButton from 'material-ui/RaisedButton/RaisedButton';
import Header from '../../components/Header/Header';

class Login extends Component {
    render() {
        return (
            <div>
                <Header />
                <div style={{
                    position: 'fixed',
                    width: '90%',
                    height: 'calc(100% - 180px - 64px)',
                    padding: '90px 5%',
                    display: 'flex',
                    backgroundColor: '#222',
                    justifyContent: 'center',
                    alignItems: 'center'
                }}>
                    <form>
                        <TextField
                            hintText="Логін"
                        /><br />
                        <TextField
                            hintText="Пароль"
                        /><br />
                        <RaisedButton
                            label="Вхід"
                            backgroundColor="rgb(96, 123, 136)"
                            style={{
                                width: '100%',
                                color: 'white'
                            }}
                        />
                    </form>
                </div>
            </div>
        );
    }
}

export default Login;
