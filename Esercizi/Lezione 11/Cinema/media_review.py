# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. 
# Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto.

# Esempio di riassunto:
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
# aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
class Media:
    def __init__(self, reviews: list[int]) -> None:
        self.reviews: list[int]=reviews
    def set_title(self, title: str) -> None:
        self.title=title
    def get_title(self) -> str:
        return self.title
    def aggiungiValutazione(self, voto: int) -> None:
        self.reviews.append(voto)
    def getMedia(self) -> float:
        return round(sum(self.reviews)/len(self.reviews), 1)
    def getRate(self) -> str:
        global ratings
        ratings={1: 'Terribile', 2: 'Brutto', 3: 'Normale', 4: 'Bello', 5: 'Grandioso'}
        return ratings[round(self.getMedia())]
    def ratePercentage(self, voto: int) -> float:
        return round(len([i for i in self.reviews if i==voto])/len(self.reviews)*100, 2)
    def recensione(self) -> None:
        print(f'Titolo del film: {self.title}',\
              f'Voto medio: {self.getMedia()}',\
              f'Giudizio: {self.getRate()}',\
              f'Terribile: {self.ratePercentage(1)}%',\
              f'Brutto: {self.ratePercentage(2)}%',\
              f'Normale: {self.ratePercentage(3)}%',\
              f'Bello: {self.ratePercentage(4)}%',\
              f'Grandioso: {self.ratePercentage(5)}%', sep='\n')

class Film(Media):
    def __init__(self, reviews: list[int]) -> None:
        super().__init__(reviews)

film1=Film([1, 2, 4, 4, 4, 5, 5, 5, 5, 3])
film1.set_title('The Shawshank Redemption')
film1.recensione()