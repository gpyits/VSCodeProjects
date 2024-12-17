-- QUERY 1:
select id, nome, cognome, posizione, stipendio
from persona
where stipendio <= 40000;

-- QUERY 2:
select id, nome, cognome, stipendio
from persona
where posizione = 'Ricercatore'
and stipendio <= 40000;

-- QUERY 3:
select sum(budget) as budget_totale
from progetto;

-- QUERY 4:
select p.nome, p.cognome, sum(pr.budget) as budget_totale
from persona p join attivitaprogetto ap on p.id = ap.persona
join progetto pr on ap.progetto = pr.id
group by p.nome, p.cognome;

-- QUERY 5:
select p.nome, p.cognome, count(distinct ap.progetto) as numero_progetti
from persona p join attivitaprogetto ap on p.id = ap.persona
where p.posizione = 'Professore Ordinario'
group by p.nome, p.cognome;

-- QUERY 6:
select p.nome, p.cognome, count(*) as numero_assenze
from persona p join assenza a on p.id = a.persona
where p.posizione = 'Professore Associato'
and a.tipo = 'Malattia'
group by p.nome, p.cognome;

-- QUERY 7:
select p.nome, p.cognome, sum(oredurata) as numero_ore
from persona p join attivitaprogetto ap on p.id = ap.id
where ap.progetto = '5'
group by p.nome, p.cognome;

-- QUERY 8:
select p.nome, p.cognome, avg(ap.oredurata) as media_ore
from persona p join attivitaprogetto ap on p.id = ap.persona
group by p.nome, p.cognome;

-- QUERY 9:
select p.nome, p.cognome, sum(anp.oredurata) as numero_ore
from persona p join attivitanonprogettuale anp on p.id = anp.persona
where anp.tipo = 'Didattica'
group by p.nome, p.cognome;

-- QUERY 10:
select p.id, sum(ap.oredurata) as numero_ore
from persona p join attivitaprogetto ap on p.id = ap.persona
where ap.wp = '5' and ap.progetto = '3'
group by p.id;
