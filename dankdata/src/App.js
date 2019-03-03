import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';
import BarChart from './BarChart'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
            <BarChart/>
        </header>
      </div>
    );
  }
}

export default App;
