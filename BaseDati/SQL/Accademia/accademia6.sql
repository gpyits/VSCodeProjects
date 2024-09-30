-- 1. Quanti sono gli strutturati di ogni fascia?
select posizione, count(*)
from persona
group by posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(*)
from persona
where stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*)
from progetto
where budget > 50000
and fine < current_date;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’?
select avg(a.oreDurata), max(a.oreDurata), min(a.oreDurata)
from attivitaprogetto a join progetto p on a.progetto = p.id
where p.nome = 'Pegasus';

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
--    ‘Pegasus’ da ogni singolo docente?
select pr.id, pr.nome, pr.cognome, avg(a.oreDurata), max(a.oreDurata), min(a.oreDurata)
from persona pr join attivitaprogetto a on pr.id = a.persona
join progetto p on p.id = a.progetto
where p.nome = 'Pegasus'
group by (a.persona, pr.nome, pr.cognome, pr.id);

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select pr.id, pr.nome, pr.cognome, sum(oreDurata)
from attivitanonprogettuale a join persona pr on a.persona = pr.id
where a.tipo = 'Didattica'
group by (pr.id, pr.nome, pr.cognome, oreDurata);
 
-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select avg(stipendio), max(stipendio), min(stipendio)
from persona
where posizione = 'Ricercatore';

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?
select posizione, avg(stipendio), max(stipendio), min(stipendio)
from persona
group by posizione;

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
select p.id, p.nome, sum(oreDurata)
from attivitaprogetto a join persona pr on a.persona = pr.id
join progetto p on p.id = a.progetto
where pr.nome = 'Ginevra' and pr.cognome = 'Riva'
group by (p.id, p.nome);

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
select p.id, p.nome
from progetto p join attivitaprogetto a on p.id = a.progetto
join persona pr on pr.id = a.persona 
group by (p.id, p.nome)
having count(distinct pr.id) > 2;

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
select p.id, p.nome, p.cognome
from persona p join attivitaprogetto a on a.persona = p.id
where p.posizione = 'Professore Associato'
group by (p.id, p.nome, p.cognome)
having count(a.persona) > 1;