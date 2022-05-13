import { Home } from '../pages';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Nav, Navbar } from 'react-bootstrap';
import React from 'react';
import './style.scss';


function NavigationBar() {
    return (
        <Router>
            <div>
                <Navbar
                    className='navigation-bar'
                    collapseOnSelect
                >
                        <Nav>
                        <Nav.Item>
                            <Nav.Link>
                                    <span className='navigation-link'
                                    onClick={() => {
                                        const anchor = document.querySelector('#home')
                                        anchor.scrollIntoView({ behavior: 'smooth', block: 'start' })
                                       }}>
                                        Home
                                    </span>
                            </Nav.Link>
                            </Nav.Item>
                        <Nav.Item>
                            <Nav.Link>
                                    <span className='navigation-link'
                                    onClick={() => {
                                        const anchor = document.querySelector('#nfts')
                                        anchor.scrollIntoView({ behavior: 'smooth', block: 'start' })
                                       }}>
                                        NFTS
                                    </span>
                            </Nav.Link>
                            </Nav.Item>
                        </Nav>
                </Navbar>

                <Switch>
                    <Route exact path='/' component={Home} />
                </Switch>
            </div>
        </Router>
    );
}

export default NavigationBar;