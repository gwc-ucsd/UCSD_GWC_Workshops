import React from 'react';
import './App.scss';
import NavigationBar from './components/navigation-bar';

function App() {  
  return (
    <div className="App">
      <div className="content-wrap">
        <header>
          <NavigationBar styles={{position: 'fixed', top: 0, width: '100%'}} />
        </header>
      </div>
    </div>
  );
}

export default App;
