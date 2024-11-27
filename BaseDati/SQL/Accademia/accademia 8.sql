--1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei giorni in cui non avevano alcuna attivita (progettuali o non progettuali)

with Elenco_persone_assenti as (
    select  ass.persona as id, ass.giorno as giorno
    from Assenza ass, AttivitaProgetto ap, AttivitaNonProgettuale anp
    where ass.persona = ap.persona and ass.persona = anp.persona and (ass.giorno = ap.giorno or ass.giorno = anp.giorno)
)
select distinct p.id, p.nome, p.cognome
from Persona p, Elenco_persone_assenti epa
where p.id <> epa.id
order by p.id asc;

--2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad alcun progetto durante la durata del progetto “Pegasus”?

select distinct p.id, p.nome, p.cognome 
from Persona p
where p.id not in (
    select distinct ap.persona as id_persona
    from AttivitaProgetto ap, Progetto p 
    where p.nome = 'Pegasus' and p.inizio <= ap.giorno and ap.giorno <= p.fine
)
order by id asc;
--3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore di tutti i professori (associati e ordinari)?

with max_stipendio as (
    select max(p1.stipendio) as stipendio_associati, max(p2.stipendio) as stipendio_ordinari
    from Persona p1, Persona p2
    where p1.posizione = 'Professore Associato' and p2.posizione = 'Professore Ordinario'
)
select * 
from Persona p, max_stipendio
where p.stipendio > max_stipendio.stipendio_associati and p.stipendio > max_stipendio.stipendio_ordinari;

--4. Quali sono le persone che hanno lavorato su progetti con un budget superiore alla media dei budget di tutti i progetti?

with Progetto_media as (
    select *
    from AttivitaProgetto ap, Progetto pr
    where ap.progetto = pr.id and pr.budget > (
        select avg(pr2.budget)
        from Progetto pr2
    )
)
select p.nome, p.cognome, p.id
from Persona p, Progetto_media pm 
where p.id = pm.persona;

--5. Quali sono i progetti con un budget inferiore allala media, ma con un numero complessivo di ore dedicate alle attività di ricerca sopra la media?

with prog_richiesti as (
    select ap.progetto, ap.tipo, sum(ap.oreDurata) as somma_ore
    from AttivitaProgetto ap 
    where ap.tipo = 'Ricerca e Sviluppo'
    group by ap.progetto, ap.tipo
)
select pr1.id, pr1.nome 
from Progetto pr1, prog_richiesti prr
where pr1.id = prr.progetto and prr.somma_ore > (
    select avg(ap.oreDurata) as media_ricerca
    from AttivitaProgetto ap
    where ap.tipo = 'Ricerca e Sviluppo'
) and pr1.budget < (
    select avg(pr.budget) as media_budget
    from  Progetto pr
);