'''
### Creazione di Test Case con UnitTest
Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Film, Azione, Commedia, Dramma, e Noleggio. 

Istruzioni
Creare un nuovo file Python denominato "test_blockbuster.py".
Importare il modulo unittest e tutte le classi definite.
Creare una sola classe di test chiamata TestFilm che eredita da unittest.TestCase.
 
Configurazione Iniziale:
- Utilizzare il metodo setUp per creare l'ambiente di test:
   - In setUp, istanziare 10 film (5 di azione, 4 commedie e 1 drammatico) e aggiungerli a una lista di film.
   - Creare un oggetto Noleggio utilizzando la lista di film creata.

Testare la Disponibilità di un Film (isAvaible):
- Scrivere un test per verificare che un film disponibile ritorni True.
- Scrivere un test per verificare che un film non disponibile ritorni False.

Testare il Noleggio di un Film (rentAMovie):
- Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
- Dopo il noleggio, verificare che il film non sia più disponibile.
- Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.

Testare il Noleggio di un Film Non Disponibile:
- Noleggiare un film con un cliente.
- Provare a noleggiare lo stesso film con un altro cliente e verificare che non sia possibile.

Testare la Restituzione di un Film (giveBack):
- Noleggiare un film e poi restituirlo.
- Verificare che il film restituito sia nuovamente disponibile.
- Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.

Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
- Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi (azione, commedia, dramma).

Testare la Stampa dei Film Disponibili (printMovies):
- Verificare che la lista dei film disponibili contenga i titoli corretti.

Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
- Noleggiare uno o più film per un cliente.
- Verificare che la stampa dei film noleggiati contenga i titoli corretti.
'''
import unittest
from blockbuster import *