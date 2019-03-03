import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
          <div className="header">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                Dank Data
            </header>
          </div>

      </div>
    );
  }
}

export default App;
