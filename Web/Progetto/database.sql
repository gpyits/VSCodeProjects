CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID univoco per ogni utente
    username TEXT NOT NULL UNIQUE,         -- Nome utente (unico)
    email TEXT NOT NULL UNIQUE,            -- Email (unica)
    password TEXT NOT NULL,                -- Password (criptata)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Data di creazione account
);

INSERT INTO users (username, email, password) 
VALUES ('Giovanni Bianchi', 'giovanni.bianchi@example.com', 'M@rvelousP@ssword2025');

INSERT INTO users (username, email, password) 
VALUES ('Sofia Conti', 'sofia.conti@example.com', 'C0ntentS3cure#456');

INSERT INTO users (username, email, password) 
VALUES ('Luca Romano', 'luca.romano@example.com', 'S@fetyIsKey789!');

INSERT INTO users (username, email, password) 
VALUES ('Alessia Ferrari', 'alessia.ferrari@example.com', 'F@stTrack#1011');

INSERT INTO users (username, email, password) 
VALUES ('Matteo Greco', 'matteo.greco@example.com', 'P@ssword1234$');
