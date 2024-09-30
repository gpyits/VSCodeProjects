-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?
select ap.codice, ap.nome, count(distinct a.comp)
from aeroporto ap join arrpart a on ap.codice = a.arrivo or ap.codice = a.partenza
group by (ap.codice, ap.nome);

-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?
select count(*)
from arrpart a join volo v on a.codice = v.codice
where a.partenza = 'HTR' and v.durataminuti >= 100;

-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?
select l.nazione, count(distinct l.aeroporto)
from luogoaeroporto l join arrpart a on l.aeroporto = a.partenza or l.aeroporto = a.arrivo
where a.comp = 'Apitalia'
group by l.nazione;

-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?
select avg(durataminuti), max(durataminuti), min(durataminuti)
from volo
where comp = 'MagicFly';

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?
select ap.codice, ap.nome, min(c.annofondaz)
from aeroporto ap join arrpart a on ap.codice = a.arrivo or ap.codice = a.partenza
join compagnia c on a.comp = c.nome
group by (ap.codice, ap.nome);

-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?
select l1.nazione, count(distinct l2.nazione)
from luogoaeroporto l1 join arrpart a on l1.aeroporto = a.partenza
join luogoaeroporto l2 on l2.aeroporto = a.arrivo and l2.nazione <> l1.nazione
group by l1.nazione;

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
select ap.codice, ap.nome, avg(v.durataminuti)
from aeroporto ap join arrpart a on ap.codice = a.partenza
join volo v on v.codice = a.codice
group by (ap.codice, ap.nome);

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?
select distinct c.nome, sum(v.durataminuti)
from volo v join compagnia c on v.comp = c.nome
where c.annofondaz > 1950
group by c.nome;

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?
select ap.codice, ap.nome
from aeroporto ap join arrpart a on ap.codice = a.partenza or ap.codice = a.arrivo
group by (ap.codice, ap.nome)
having count(distinct a.comp) = 2;

-- 10. Quali sono le città con almeno due aeroporti?
select citta
from luogoaeroporto
group by citta
having count(*) >= 2;

-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
-- ore?
select c.nome
from compagnia c join volo v on c.nome = v.comp
group by c.nome
having avg(v.durataminuti) > 360;

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
-- minuti?
select comp
from volo
group by (comp)
having min(durataminuti) > 100;