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


-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.


-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
-- rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

