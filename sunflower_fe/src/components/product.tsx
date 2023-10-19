import React from 'react';
import Card from 'react-bootstrap/Card';

const ProductImageStyle = {
    width: '8rem',
    height: '8rem',
    margin: 'auto',
    padding: '0.25rem',
};
const ProductCardStyle = {
    margin: '0 0.1rem 1rem 0.1rem',
};
const CenterStyle = {
    margin: 'auto',
};

function Product(props:any) {
    const {id, name, quantity, size} = props;
    return (
        <Card style={ProductCardStyle}>
            <Card.Img variant="top" src="https://www.bolster.eu/media/images/5460_dbweb.jpg?1549350221" alt={name} style={ProductImageStyle}/>
            <Card.Body style={CenterStyle}>
                <Card.Title style={CenterStyle}>
                    {name} {id}
                </Card.Title>
                <Card.Text style={CenterStyle}>
                    Size: {size}
                </Card.Text>
                <Card.Text style={CenterStyle}>
                    Quantity: {quantity}
                </Card.Text>
            </Card.Body>
        </Card>
    )
};

export default Product;
