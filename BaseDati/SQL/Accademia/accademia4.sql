-- Quali sono i cognomi distinti di tutti gli strutturati?
select distinct p.cognome
from Persona p;

-- Quali sono i ricercatori (con nome e cognome)?
select p.cognome, p.nome
from Persona p
where p.posizione = 'Ricercatore';

-- Quali sono i professori associati il cui cognome inizia con la lettera V?
select p.cognome
from Persona p
where p.cognome like 'V%'
and p.posizione = 'Professore Associato';

-- Quali sono i professori associati e ordinari il cui cognome inizia con la lettera V?
select p.cognome
from Persona p
where p.cognome like 'V%'
and p.posizione <> 'Ricercatore';

-- Quali sono i progetti già terminati in data odierna?
select p.fine
from Progetto p 
where p.fine < CURRENT_DATE;

-- Quali sono i nomi di tutti i progetti ordinati in ordine crescente di data di inizio?
select p.nome, p.inizio
from Progetto p
order by inizio;

-- Quali sono i nomi dei WP ordinati in ordine crescente per nome?
select wp.nome
from WP
order by nome;

--Quali sono le distine cause di assenza di tutti gli strutturati?
select distinct a.tipo as tipo
from Assenza as a;

-- Quali sono le distinte tiplogie i attività di progetto di tutti gli strutturati?
select distinct a.tipo as tipo
from AttivitaProgetto as a;

-- Quali sono i giorni distinti nei quali del personale ha effettuato attività non progettuali di tipo "Didattica?"
select distinct a.giorno
from AttivitaNonProgettuale as a
where a.tipo = 'Didattica';