-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select codice, comp
from Volo
where durataMinuti > 180;

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct comp
from Volo
where durataMinuti > 180;

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?
select codice, comp
from ArrPart
where partenza = 'CIA';

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?
select codice, comp
from ArrPart
where arrivo = 'FCO';

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?
select codice, comp
from ArrPart
where partenza = 'FCO'
and arrivo = 'CIA';

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?
select codice, comp
from ArrPart
where partenza = 'FCO'
and arrivo = 'JFK';

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?
select a.comp
from ArrPart a, LuogoAeroporto l1, LuogoAeroporto l2
where l1.aeroporto = a.partenza and l2.aeroporto = a.arrivo
and l1.citta = 'Roma' and l2.citta = 'New York';

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?
select distinct a.codice, a.nome, l.luogo
from Aeroporto a, LuogoAeroporto l, ArrPart p
where p.partenza = a.nome and p.comp = 'MagicFly'

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.
select a.codice, a.comp, a.partenza, a.arrivo
from ArrPart a, LuogoAeroporto l1, LuogoAeroporto l2
where l1.aeroporto = a.partenza and l2.aeroporto = a.arrivo
and l1.citta = 'Roma' and l2.citta = 'New York';

-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.
select c.nome as compagnia, a1.codice as volo1, a2.codice as volo2, l1.citta as partenza, l3.citta as scalo, l2.citta as arrivo
from ArrPart a1
join ArrPart a2 on a1.arrivo = a2.partenza
join Compagnia c on a1.comp = c.nome and a2.comp = c.nome
join LuogoAeroporto l1 on a1.partenza = l1.aeroporto
join LuogoAeroporto l2 on a2.arrivo = l2.aeroporto
join LuogoAeroporto l3 on a1.arrivo = l3.aeroporto
where l1.citta = 'Roma'
and l2.citta = 'New York'
and l3.citta != 'Roma' and l3.citta != 'New York';

-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
-- rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?
select c.nome as compagnia
from ArrPart a
join Compagnia c on a.comp = c.nome
join LuogoAeroporto l1 on a.partenza = l1.aeroporto
join LuogoAeroporto l2 on a.arrivo = l2.aeroporto
where l1.aeroporto = 'FCO'
and l2.aeroporto = 'JFK';