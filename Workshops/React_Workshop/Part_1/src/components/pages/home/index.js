import cover from 'assets/images/cover.webp';
import React from 'react';
import './style.scss';

export function Home() {

    return (
    <div>
        <section id='home' className='section-container'>
        <div className="App-container">
          <img src={cover} className="App-logo" alt="logo" />
          <h1 className="App-overlay-title">Welcome to our NFTS Website!</h1>
        </div>
        <p className='intro-text'>Here you'll be able to look at your favorite NFTS and learn react!</p>
          <a    className='link-text'
                href="https://reactjs.org/tutorial/tutorial.html">
              Click here to learn more about react
            </a>
        </section>
        
    </div> 
    );
}
