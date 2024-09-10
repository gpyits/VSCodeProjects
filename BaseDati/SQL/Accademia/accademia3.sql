create database accademia;

--connetti al db
\c accademia

create type Strutturato as 
    enum('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as 
    enum('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as 
    enum('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as 
    enum('Chiusura Universitaria', 'Maternita', 'Malattia');

create domain PosInteger as integer
    default 0
    check (value>=0);

create domain StringaM as
    varchar(100);

create domain NumeroOre as integer
    default 0
    check (value>=0 and value <=8);

create domain Denaro as integer
    default 0
    check (value>=0);

create table Persona
(
    id PosInteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null,
    primary key (id)
);

create table Progetto
(
    id PosInteger not null primary key,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    unique (nome),
    check (fine>inizio)
);

create table WP
(
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    primary key (id, progetto),
    unique (progetto, nome),
    foreign key (progetto) references Progetto(id),
    check (fine>inizio)
);

create table AttivitaProgetto
(
    id PosInteger not null primary key,
    persona PosInteger not null,
    foreign key (persona) references Persona(id),
    progetto PosInteger not null,
    wp PosInteger not null,
    foreign key (progetto, wp) references WP(progetto, id),
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null
);

create table AttivitaNonProgettuale
(
    id PosInteger not null primary key,
    persona PosInteger not null,
    foreign key (persona) references Persona(id),
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null
);

create table Assenza
(
    id PosInteger not null primary key,
    persona PosInteger not null,
    foreign key (persona) references Persona(id),
    tipo CausaAssenza not null,
    giorno date not null,
    unique (persona, giorno)
);