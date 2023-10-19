import axios from 'axios';
import Product from './product'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import React from 'react';
import { useEffect, useState } from 'react';

const ProductCardtyle = {
    margin: 'auto',
};
const ListOfProducts = {
    paddingTop: '1rem',
};

function build_products_grid(data:any){
    let product_grid: any = [];
    let products: any = [];

    if(data){
        if (data.length>0){
            data.forEach((obj:any) => {
                products.push(
                    <Col style={ProductCardtyle} xs={12} sm={6} md={4} lg={4} xl={3} xxl={3}>
                        <Product id={obj.id} name={obj.name} quantity={obj.quantity} size={obj.size} key={obj.id+obj.name} />
                    </Col>
                )
            });
        }
    };

    product_grid.push(<Row style={ProductCardtyle}>{products}</Row>);
    console.log(product_grid);
    return product_grid;
};


function ProductList(){
    const [products, setProducts] = useState();

    useEffect(()=>{
        axios.get("http://localhost:8000/api/products/")
        .then(function (response:any){
            return response;
        })
        .then(function (response:any){
            setProducts(response.data)
        })
        .catch(function (error:any){
            console.log(JSON.stringify(error, null, 2));
        })
    }, []);

    return (
        <Container style={ListOfProducts} fluid>
            {build_products_grid(products)}
        </Container>
    )
};

export default ProductList;
