import React from 'react';
import { Container, Card } from 'react-bootstrap';

const About = () => {
  return (
    <Container className="mt-4">
      <Card>
        <Card.Body>
          <Card.Title>About</Card.Title>
          <Card.Text>
            This is a simple React app with React Bootstrap and REST API integration.
          </Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default About;