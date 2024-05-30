# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): 
#           Aggiunge uno o più film a un regista specifico nel catalogo. 
#           Se il regista non esiste, viene creato un nuovo record. 
#           Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): 
#           Rimuove un film specifico dall'elenco dei film di un regista. 
#           Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): 
#           Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): 
#           Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): 
#           Trova tutti i film che contengono una certa parola nel titolo. 
#           Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata 
#           o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
class MovieCatalogue:
    def __init__(self) -> None:
        self.movies: dict[str:list[str]]={}
    def add_movie(self, director_name: str, movies: list[str]) -> None:
        self.movies[director_name]=self.movies[director_name] if self.movies[director_name] else [] #[] if not self.movies[director_name] else self.movies[director_name]
        for movie in movies: self.movies[director_name].append(movie)
    def remove_movie(self, director_name: str, movies_name: str) -> None:
        self.movies[director_name].remove(movies_name)
        if not self.movies[director_name] and input(f'Director {director_name} does not have any movies now, do you want to remove it entirely? [y/n]').lower()=='y': 
            del self.movies[director_name] #self.movies.pop(director_name, None)
    def list_directors(self) -> None:
        print('Directors:', *[director for director in self.movies.keys()], sep='\n')
    def get_movies_by_director(self, director_name: str) -> None:
        print(f'Movies by {director_name}:', *self.movies[director_name], sep='\n')
    def search_movies_by_title(self, title: str) -> list[str]:
        searched=[]
        for movies in self.movies.keys(): 
            for movie in movies: 
                if title in movie: 
                    searched.append(movie)
        return searched if searched else 'Errore: l\'elemento selezionato non corrisponde a nessun criterio di ricerca'