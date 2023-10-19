import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function HeaderBar() {
  return (
    <Navbar expand="lg" className="bg-body-primary" style={{fontSize: "1.5em"}}>
      <Container>
        <Navbar.Brand href="/">
          <img
            src="https://www.bolster.eu/media/images/5460_dbweb.jpg?1549350221"
            width="60"
            height="60"
            className="d-inline-block align-top"
            alt="Sunflower logo"
          />
        </Navbar.Brand>
        <Navbar.Brand style={{fontSize: "2em"}} href="/">Sunflower</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="https://www.instagram.com/shirusunflower/">Instagram</Nav.Link>
            <Nav.Link href="https://www.facebook.com/shirusunflower/">Facebook</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default HeaderBar;
