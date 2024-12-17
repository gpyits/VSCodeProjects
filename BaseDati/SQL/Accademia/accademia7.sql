-- Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
select posizione, avg(stipendio) as media, stddev(stipendio) as dev_standard
from Persona
group by posizione
order by dev_standard asc;

-- Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media
-- della loro categoria?
with media_ric as (
    select posizione, avg(stipendio) as stipendio
    from Persona
    where posizione = 'Ricercatore'
    group by posizione
)

select *
from persona p join media_ric m on p.posizione=m.posizione 
where p.posizione = 'Ricercatore'
and p.stipendio > m.stipendio;

-- Per ogni categoria di strutturati quante sono le persone con uno stipendio che
-- differisce di al massimo una deviazione standard dalla media della loro categoria?
with media_ass as (
    select posizione, avg(stipendio) as stipendio
    from persona
    group by posizione
),
stddev_ass as (
    select posizione, stddev(stipendio) as stipendio
    from persona
    group by posizione
)

select p.posizione, count(*) as numero
from persona p join media_ass m on p.posizione = m.posizione
join stddev_ass s on p.posizione = s.posizione
where p.stipendio >= m.stipendio - s.stipendio
and p.stipendio <= m.stipendio + s.stipendio
group by p.posizione
order by numero asc;

-- Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
-- progettuali? Restituire tutti i loro dati e il numero di ore lavorate.
select p.id, p.nome, p.cognome, p.posizione, p.stipendio, sum(oreDurata) as ore_lavorate
from persona p join attivitaprogetto a on p.id = a.persona
group by p.id, p.nome, p.cognome, p.posizione, p.stipendio
having sum(oreDurata) >= 20;

-- Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
-- progetti? Restituire nome dei progetti e loro durata in giorni.
with med_dur as (
    select avg(fine - inizio) as durata
    from progetto
)

select p.nome, (p.fine - p.inizio) as durata_giorni
from progetto p join med_dur m on (p.fine - p.inizio) > m.durata
group by nome, durata_giorni;

-- Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo
-- “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle
-- ore dedicate a tali attività nel progetto.


-- Quali sono i professori ordinari che hanno fatto più assenze per malattia del nu-
-- mero di assenze medio per malattia dei professori associati? Restituire id, nome e
-- cognome del professore e il numero di giorni di assenza per malattia.