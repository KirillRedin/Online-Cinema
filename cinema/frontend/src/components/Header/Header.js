import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar/AppBar';
import FlatButton from 'material-ui/FlatButton/FlatButton'
import IconCinema from 'material-ui/svg-icons/action/theaters';
import {Link} from 'react-router-dom';

class Header extends Component {
    render() {
        return (
            <AppBar
                title="ProjectX Cinema"
                iconElementLeft={
                    <Link to="/">
                        <IconCinema
                            style={{
                                height: '45px',
                                width: '45px'
                            }}
                        />
                    </Link>
                }
                iconElementRight={
                    <div style={{marginTop: '5px'}}>
                        <FlatButton
                            label="Про нас"
                            labelStyle={{
                                color: '#DFF7FA'
                            }}
                            containerElement={<Link to="/aboutus"/>}
                        />
                        <FlatButton
                            label="Логін"
                            style={{
                                color: '#DFF7FA'
                            }}
                            containerElement={<Link to="/login"/>}
                        />
                    </div>
                }
                style={{
                    backgroundColor: '#607B88',
                }}
                titleStyle={{
                    textAlign: 'left',
                    color: '#DFF7FA'
                }}
            />
        );
    }
}

export default Header;
