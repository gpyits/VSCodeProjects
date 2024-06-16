'''
### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film: genere="Azione", nella classe Azione
ed un attributo privato di tipo float chiamato penale. 
I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:
    getGenere(): 
        che ritorna il genere di film

    getPenale():
        che ritorna il valore della penale

    calcolaPenaleRitardo():
        che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
'''
from film import Film

class Acion(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.fee: float=3.0
    def getGenre(self) -> str:
        return 'Azione'
    def getFee(self) -> float:
        return self.fee
    def calculateDailyFee(self, days: int) -> float:
        return days*self.fee
    def __str__(self) -> str:
        return 'genre=Action'

class Comedy(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.fee: float=2.5
    def getGenre(self) -> str:
        return 'Comedy'
    def getFee(self) -> float:
        return self.fee
    def calculateDailyFee(self, days: int) -> float:
        return days*self.fee
    def __str__(self) -> str:
        return 'genre=Comedy'
    
class Drama(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.fee: float=2.0
    def getGenre(self) -> str:
        return 'Drama'
    def getFee(self) -> float:
        return self.fee
    def calculateDailyFee(self, days: int) -> float:
        return days*self.fee
    def __str__(self) -> str:
        return 'genre=Drama'