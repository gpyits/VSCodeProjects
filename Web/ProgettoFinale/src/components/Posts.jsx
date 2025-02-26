import React, { useEffect, useState } from 'react';
import { Container, Card } from 'react-bootstrap';
import { fetchPosts } from '../api';

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const getPosts = async () => {
      const data = await fetchPosts();
      setPosts(data);
    };
    getPosts();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Posts</h1>
      {posts.map(post => (
        <Card key={post.id} className="mb-3">
          <Card.Body>
            <Card.Title>{post.title}</Card.Title>
            <Card.Text>{post.body}</Card.Text>
          </Card.Body>
        </Card>
      ))}
    </Container>
  );
};

export default Posts;