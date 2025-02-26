import React from 'react';
import { Container, Card } from 'react-bootstrap';

const Home = () => {
  return (
    <Container className="mt-4">
      <Card>
        <Card.Body>
          <Card.Title>Home</Card.Title>
          <Card.Text>
            Welcome to the Home page!
          </Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Home;