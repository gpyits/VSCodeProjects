create database out;

create table Nazione(
    nome varchar not null primary key
);

create table Regione(
    nome varchar not null primary key
);

create table citta(
    nome varchar not null primary key
);

create table sede(
    indirizzo Indirizzo not null,
    nome varchar not null
);

create table sala(
    nome varchar not null primary key
);

create table settore(
    nome varchar not null primary key
);

create table posto(
    fila PosInteger not null,
    colonna not null,
    primary key (fila, colonna),
    check (fila > 0),
    check (colonna > 0)
);

create table prenotazione(
    
);

create table utente(
    nome varchar not null,
    cognome varchar not null,
    cf CF not null primary key
);

create table evento(
    data DataOra not null primary key
);

create table spettacolo(
    
);