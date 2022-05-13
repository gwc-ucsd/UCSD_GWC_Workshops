import React from 'react';
import { Card, CardDeck } from 'react-bootstrap';
import nft1 from 'assets/images/nft1.jpg';
import nft2 from 'assets/images/nft2.jpg';
import nft3 from 'assets/images/nft3.jpg';
import './style.scss';

const nfts = [
    {
        name: 'NFT 1',
        description: 'This is the first nft',
        image: nft1,
    },
    {
        name: 'NFT 2',
        description: 'This is the second nft',
        image: nft2,
    },
    {
        name: 'NFT 3',
        description: 'This is the third nft',
        image: nft3,
    },
];

export function Nfts() {
    return (
    <div>
        <h1>NFTS</h1>
        <CardDeck>
                {nfts.map((element) => { 
                    return (
                        <div>
                        <Card className='card-box'>
                            <div className='pic-box'>
                                <Card.Img
                                    className='card-picture'
                                    src={element.image}
                                />
                            </div>
                                <p className='card-title'>{element.name}</p>
                            <p className='card-description'>{element.description}</p>
                        </Card>
                        </div>
                    );
                })}
                </CardDeck>
        </div> 
    );
}
