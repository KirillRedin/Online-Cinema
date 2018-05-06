import React, { Component } from 'react';
import {Route, Switch, BrowserRouter} from 'react-router-dom';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
import MainPage from "./pages/Main/Main";
import Login from "./pages/Login/Login";
import AboutUs from "./pages/AboutUs/AboutUs";
import Hall from "./pages/Hall/Hall";
import NotFound from "./pages/NotFound/NotFound";

class App extends Component {
    render() {
        return (
            <MuiThemeProvider muiTheme={getMuiTheme(darkBaseTheme)}>
                <BrowserRouter>
                    <Switch>
                        <Route exact path="/" component={MainPage} />
                        <Route path="/login" component={Login} />
                        <Route path="/aboutus" component={AboutUs} />
                        <Route path="/hall" component={Hall} />
                        <Route component={NotFound} />
                    </Switch>
                </BrowserRouter>
            </MuiThemeProvider>
        );
    }
}

export default App;
