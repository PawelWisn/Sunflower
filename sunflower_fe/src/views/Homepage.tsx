import React from 'react';
import Button from 'react-bootstrap/Button';
import ProductList from '../components/productList';
import HeaderBar from '../components/headerBar';

const ProductListStyle = {
    backgroundColor: 'green',
    textAlign: 'center' as const,
    flexGrow: 1,
};

const FillAllStyle = {
    display: "flex",
    flexFlow: "column",
    minHeight: "100vh",
}
function Homepage(){
    return (
        <div style={FillAllStyle}>
            <header><HeaderBar/></header>
            <main style={ProductListStyle}><ProductList/></main>
        </div>
    )
}

export default Homepage;
