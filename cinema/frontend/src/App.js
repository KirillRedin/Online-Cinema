import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Красава, Работает!!</h1>
        </header>
          <div style={{
              position: 'fixed',
              right: '10px',
              bottom: '10px',
              fontSize: '20px'
          }}>Kirill - pizduc</div>
      </div>
    );
  }
}

export default App;
