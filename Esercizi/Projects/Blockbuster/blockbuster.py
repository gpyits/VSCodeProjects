'''
### CLASSE: Film
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:
    init(id, title): 
        metodo costruttore.

    setID(id): 
        che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.

    setTitle(title): 
        che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.

    getID(): 
        che consente di ritornare il valore del codice identificativo di un film.

    getTitle(): 
        che consente di ritornare il valore del titolo di un film.

    isEqual(otherFilm): 
        che ritorna true se il codice identificativo di due film è uguale.  
 
### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) 
ed un attributo privato di tipo float chiamato penale. 
I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:
    getGenere(): 
        che ritorna il genere di film

    getPenale():
        che ritorna il valore della penale

    calcolaPenaleRitardo():
        che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
 
### CLASSE: Noleggio
In un file "noleggio.py", creare una classe Noleggio.
Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), 
un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
 
- Definire i seguenti metodi:
    init(film_list): 
        tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.

    isAvaible(film): 
        tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. 
        Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". 
        Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".

    rentAMovie(film, clientID): 
        tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. 
        Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. 
        Pertanto, il metodo deve verificare la disponibilità. 
        Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
            La chiave sarà l'id del cliente che noleggia (id_client), il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
            Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati dal cliente dato.  
            Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!". 
            Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".

    giveBack(film, clientID, days): 
        questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, 
        il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se. 
        Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, 
        deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). 
        Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. 
        Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".

    printMovies(): 
        stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"

    printRentMovies(clientID): 
        questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
'''
class Film:
    def __init__(self, id: int, title: str) -> None:
        self.__id: int=id
        self.__title: str=title
    def setId(self, id: int) -> None:
        self.__id=id
    def setTitle(self, title: str) -> None:
        self.__title=title
    def getID(self) -> int:
        return self.__id
    def getTitle(self) -> str:
        return self.__title
    def isEqual(self, otherFilm: 'Film') -> bool:
        return True if self.getID()==otherFilm.getID() else False

class Action(Film):
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
    
class Rental:
    def __init__(self, film_list: list[Film]) -> None:
        self.film_list: list[Film]=film_list
        self.rented_films: dict[int:list[Film]]={}
    def isAvailable(self, film: Film) -> bool:
        if film in self.film_list: print(f'The chosen film "{film.getTitle()}" is available'); return True
        else: print(f'The chosen film "{film.getTitle()}" is not available'); return False
    def rentAMovie(self, film: Film, clientID: int) -> None:
        try:
            self.rented_films[clientID]
            if self.isAvailable(film):
                self.rented_films[clientID].append(film), self.film_list.remove(film)
                print(f'Client {clientID} rented "{film.getTitle()}"'); return
        except KeyError: self.rented_films[clientID]=[]; return self.rentAMovie(film, clientID)
        print(f'Client {clientID} couldn\'t rent "{film.getTitle()}"')
    def giveBack(self, clientID: int, film: Film, days: int) -> None:
        try: 
            if film in self.rented_films[clientID]:
                self.rented_films[clientID].remove(film), self.film_list.append(film)
                print(f'Film {film.getTitle()} returned, client {clientID} must pay {film.calculateDailyFee(days)}'); return
        except KeyError: self.rented_films[clientID]=[]; return self.giveBack(film, clientID, days)
        print(f'Client {clientID} couldn\'t return "{film.getTitle()}"')
    def printMovies(self) -> None:
        print('\nMovies:',*[f'{film.getTitle()} - '+str(film) for film in self.film_list], '',sep='\n') if self.film_list else print('\nMovies: []\n')
    def printRentedMovies(self, clientID: str) -> None:
        try: print(f'\nRented movies by client {clientID}:', *[f'{film.getTitle()} - '+str(film) for film in self.rented_films[clientID]], sep='\n') if self.rented_films else print(f'\nRented movies by client {clientID}:\n[]')
        except KeyError: print(f'Rented movies by client {clientID}:\n[]\n')