import React, { useState } from "react";
import './App.css'

function App() {
  // Stato per memorizzare gli utenti
  const [users, setUsers] = useState([]);

  // Funzione per fare la richiesta agli utenti
  const fetchUsers = async () => {
    try {
      const response = await fetch("http://localhost:5173/api/users"); // URL dell'API Flask
      const data = await response.json();
      setUsers(data); // Imposta gli utenti nel state
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  return (
    <div className="App">
      <h1>Users List</h1>
      <button onClick={fetchUsers}>Mostra utenti</button> {/* Bottone per fetch */}
      <table>
        <thead>
          <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Created At</th>
          </tr>
        </thead>
        <tbody>
          {users.length > 0 ? (
            users.map(user => (
              <tr key={user.id}>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.created_at}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3">No users found.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
