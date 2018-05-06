import React, { Component } from 'react';
import axios from 'axios';
import TextField from 'material-ui/TextField/TextField';
import RaisedButton from 'material-ui/RaisedButton/RaisedButton';
import Header from '../../components/Header/Header';

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            name: ''
        }
    }

    handleSubmit = () => {
        const { email, name } = this.state;
        const { bookType, placeId } = this.props.match.params;
        axios.post('/api/book', {
            email: email,
            name: name,
            statusId: +bookType,
            placeId: +placeId
        })
            .then(function (response) {
                console.log('krasava');
            })
            .catch(function (error) {
                console.log('ploho');
            });
    };

    handleChange = (e, type) => {
        if (type === 'email')
            this.setState({ email: e.target.value});
        else this.setState({ name: e.target.value});

    };

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
                        <div style={{ color: 'rgba(255, 255, 255, 0.5)', fontSize: '18px' }}>Введіть свої дані</div>
                        <TextField
                            hintText="Email"
                            type="email"
                            value={this.state.email}
                            onChange={(e) => this.handleChange(e, 'email')}
                        /><br />
                        <TextField
                            hintText="Ім'я"
                            value={this.state.name}
                            onChange={(e) => this.handleChange(e, 'name')}
                        /><br />
                        <RaisedButton
                            onClick={this.handleSubmit}
                            label={!+this.props.match.params.bookType ? 'Забронювати' : 'Сплатити'}
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
