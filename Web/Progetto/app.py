import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

# Endpoint per ottenere tutti gli utenti
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()  # Ottieni tutti gli utenti
    conn.close()

    # Converte i dati in formato JSON
    users_list = [{"id": user[0], "username": user[1], "email": user[2], "created_at": user[4]} for user in users]
    
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True, port="5173")
