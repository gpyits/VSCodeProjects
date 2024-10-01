create table Nazione(
    nome varchar not null primary key,
);

create table Regione(
    nome varchar not null primary key
    reg_naz varchar not null primary key,
        foreign key (reg_naz) references Nazione(nome)
);

create table Citta(
    nome varchar not null primary key,
    citta_reg varchar not null primary key,
        foreign key (citta_reg) references Regione(nome)
);

create table Officina(
    nome varchar not null,
    indirizzo Indirizzo not null,
    id PosInteger not null primary key,
    citta_off varchar not null primary key,
        foreign key (citta_off) references Citta(nome),
);

create table Riparazione(
    riconsegna timestamp[0..1] not null,
    codice PosInteger not null primary key,
    inizio timestamp not null,
    off_rip PosInteger not null primary key,
        foreign key (off_rip) references Officina(id)
);