-- 1 Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
-- ‘Pegasus’ ?
select wp.nome, wp.inizio, wp.fine
from wp, progetto p
where wp.progetto = p.id
and p.nome = 'Pegasus'


-- 2 Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
select distinct s.nome, s.cognome, s.posizione
from attivitaprogetto ap, progetto p, persona s
where ap.progetto = p.id 
and ap.persona = s.id
and p.nome = 'Pegasus';


-- 3 Quali sono il nome, il cognome e la posizione degli strutturati che hanno 
-- più di una attività nel progetto ‘Pegasus’?
-- Quali sono il nome, il cognome e la posizione degli strutturati che
-- hanno almeno due attività distinte nel progetto 'Pegasus'?
-- Quali sono il nome, il cognome e la posizione degli strutturati che
-- hanno almeno una coppia di attività distinte nel progetto 'Pegasus'?
select distinct s.id, s.nome, s.cognome, s.posizione
from attivitaprogetto a1, attivitaprogetto a2, persona s, progetto p
where a1.id <> a2.id 
and a1.progetto = a2.progetto
and a1.persona = a2.persona
and a1.persona = s.id
and a1.progetto = p.id
and p.nome = 'Pegasus';


-- 4 Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?
select distinct s.id, nome, cognome, posizione 
from assenza a, persona s
where a.persona = s.id
and tipo = 'Malattia' 
and posizione = 'Professore Ordinario';


-- 5 Quali sono il nome, il cognome e la posizione dei Professori Ordinari 
-- che hanno fatto più di una assenza per malattia?
select distinct s.id, s.nome, s.cognome
from persona s, assenza a1, assenza a2
where a1.persona = s.id
select Persona.nome, Persona.cognome, Persona.posizione

--6
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale a
where p.id = a.persona
and p.posizione = 'Ricercatore'
and a.tipo = 'Didattica';

-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale a1, AttivitaNonProgettuale a2, AttivitaNonProgettuale a3
where a1.id <> a2.id
and a1.tipo = 'Didattica'
and a2.tipo = 'Didattica'
and a1.persona = s.id
and a2.persona = s.id 
and a2 = p.id
and p.posizione = 'Ricercatore';

-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?
select distinct Persona.nome, Persona.cognome
from Persona
join AttivitaProgetto on Persona.id = AttivitaProgetto.persona
join AttivitaNonProgettuale on Persona.id = AttivitaNonProgettuale.persona
where AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;

-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività.
select Persona.nome, Persona.cognome, AttivitaProgetto.giorno, Progetto.nome, AttivitaNonProgettuale.tipo, AttivitaProgetto.oreDurata, AttivitaNonProgettuale.oreDurata
from Persona
join AttivitaProgetto on Persona.id = AttivitaProgetto.persona
join AttivitaNonProgettuale on Persona.id = AttivitaNonProgettuale.persona
join Progetto on AttivitaProgetto.progetto = Progetto.id
where AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;

-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?
select distinct Persona.nome, Persona.cognome
from Persona
join assenza on Persona.id = assenza.persona
join AttivitaProgetto on Persona.id = AttivitaProgetto.persona
where assenza.giorno = AttivitaProgetto.giorno;

-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
select Persona.nome, Persona.cognome, assenza.giorno, Progetto.nome, assenza.tipo, AttivitaProgetto.oreDurata
from Persona
join assenza on Persona.id = assenza.persona
join AttivitaProgetto on Persona.id = AttivitaProgetto.persona
join Progetto on AttivitaProgetto.progetto = Progetto.id
where assenza.giorno = AttivitaProgetto.giorno;

-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
select distinct wp1.nome, p1.nome, p2.nome
from WP wp1, WP wp2, Progetto p2
where wp1.progetto = p1.id
and wp1.nome = wp2.nome
and wp1.progetto <> wp2.progetto
and wp2.progetto = p2.id;