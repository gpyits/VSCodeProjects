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

class TestFilm(unittest.TestCase):
   def setUp(self) -> None:
      self.john_wick=Action(1222015, 'John Wick')
      self.fast_furious=Action(432009, 'Fast&Furious')
      self.top_gun=Action(9251986, 'Top Gun')
      self.goldfinger=Action(3251965, 'Goldfinger')
      self.private_ryan=Action(10301988, 'Saving Private Ryan')
      self.sole_catinelle=Comedy(10312013, 'Sole a Catinelle')
      self.meet_parents=Comedy(222001, 'Meet the Parents')
      self.benvenuti_sud=Comedy(1012010, 'Benvenuti al Sud')
      self.spy_kids=Comedy(7252003, 'Spy Kids 3D: Game Over')
      self.the_godfather=Drama(3241972, 'The Godfather')
      self.taxi_driver=Drama(8271976, 'Taxi Driver')
      self.rental=Rental([self.john_wick, self.fast_furious, self.top_gun, self.goldfinger, self.private_ryan, 
                          self.sole_catinelle, self.meet_parents, self.benvenuti_sud, self.spy_kids, 
                          self.the_godfather])
   def test_isAvailable(self) -> None:
      print(' Test: isAvailable')
      self.assertEqual(self.rental.isAvailable(self.private_ryan), True)
      self.assertEqual(self.rental.isAvailable(self.taxi_driver), False)
   def test_rentAMovie(self) -> None:
      print(' Test: rentAMovie')
      self.rental.rentAMovie(self.the_godfather, 0)
      self.assertEqual(self.rental.isAvailable(self.the_godfather), False)
      self.assertNotEqual(self.rental.rented_films[0], [])
      self.rental.rentAMovie(self.the_godfather, 1)
      self.assertEqual(self.rental.rented_films[1], [])
   def test_giveBack(self) -> None:
      print(' Test: giveBack')
      self.rental.rentAMovie(self.the_godfather, 0)
      self.rental.giveBack(0, self.the_godfather, 1)
      self.assertEqual(self.rental.rented_films[0], [])
   def test_fee(self) -> None:
      self.assertEqual(self.john_wick.calculateDailyFee(10), 30)
      self.assertEqual(self.sole_catinelle.calculateDailyFee(4), 10)
      self.assertEqual(self.taxi_driver.calculateDailyFee(2), 4)
   def test_printMovies(self) -> None:
      print(' Test: printMovies')
      self.rental.rentAMovie(self.the_godfather, 0)
      self.rental.rentAMovie(self.the_godfather, 1)
      self.rental.rentAMovie(self.taxi_driver, 1)
      self.rental.rentAMovie(self.meet_parents, 1)
      self.assertEqual(len(self.rental.film_list), 8)
      self.rental.printMovies()
   def test_printRentedMovies(self) -> None:
      print(' Test: printRentedMovies')
      self.rental.rentAMovie(self.the_godfather, 0)
      self.rental.rentAMovie(self.taxi_driver, 0)
      self.rental.rentAMovie(self.private_ryan, 0)
      self.assertEqual(len(self.rental.rented_films[0]), 2)
      self.rental.printRentedMovies(0)
      self.rental.printRentedMovies(1)

if __name__=='__main__':
    unittest.main()