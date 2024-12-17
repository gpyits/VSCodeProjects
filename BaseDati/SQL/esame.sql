create domain Voto as Integer
    default 0
    check (value >= 0 and value <= 5);

create table Utente (
    nome varchar(100) not null primary key
);

create table Video (
    id serial not null primary key,
    titolo varchar(100) not null,
    descrizione varchar(100) not null,
    istante timestamp not null,
    ragioneCensura varchar(100),
    istanteCensura timestamp
);

create table Tag (
    id serial not null primary key,
    nome varchar(100) not null
);

create table Valutazione (
    id serial not null primary key,
    voto Voto not null,
    istante timestamp not null,
    utente_nome varchar(100) not null,
    foreign key (utente_nome) references Utente(nome),
    video_id integer not null,
    foreign key (video_id) references Video(id)
);

create table video_tag (
    video_id integer not null,
    foreign key (video_id) references Video(id),
    tag_id integer not null,
    foreign key (tag_id) references Tag(id),
    primary key (video_id, tag_id)
);