# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
# Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
# Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

# Classi:
# - Film: Rappresenta un film con titolo e durata.

# - Sala: 
#     Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
#     Metodi:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.

# - Cinema: 
#     Gestisce le operazioni legate alla gestione delle sale.
#     Metodi:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

# Test case:
# - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.

# - Un cliente sceglie un film e prenota un certo numero di posti.

# - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
class Movie:
    def __init__(self, title: str, duration: str) -> None:
        self.title: str=title
        self.duration: int=duration

class Room:
    def __init__(self, id: int, current_movie: Movie, total_seats: int, taken_seats: int= 0) -> None:
        self.id: int=id
        self.current_movie: Movie=current_movie
        self.total_seats: int=total_seats
        self.taken_seats: int= taken_seats
    def book_seats(self, seats: int) -> str:
        if self.taken_seats+seats<=self.total_seats and seats>=0:
            self.taken_seats+=seats
            return f'Booked {seats} seats for {self.current_movie.title}. Available seats: {self.total_seats-self.taken_seats}'
        else:
            return f'Error: cannot book {seats} seats. Available seats: {self.total_seats-self.taken_seats}'
    def available_seats(self) -> int:
        return self.total_seats-self.taken_seats

class Theater:
    def __init__(self, rooms: list[Room]=[]) -> None:
        self.rooms: Room=rooms
    def add_room(self, room: Room) -> None:
        self.rooms.append(room)
    def book_movie(self, movie_title: str, seats: int) -> str:
        for room in self.rooms:
            if room.current_movie.title==movie_title:
                return room.book_seats(seats)
    
theater=Theater([Room(1, Movie('Planet of the Apes', '1h52m'), 50), Room(2, Movie('Interstellar', '2h49m'), 50), Room(3, Movie('The Lighthouse', '1h50m'), 50)])
print(theater.book_movie('The Lighthouse', 49),\
      theater.book_movie('Planet of the Apes', 20),\
      theater.book_movie('Planet of the Apes', -20), theater.book_movie('Planet of the Apes', 30),\
      theater.book_movie('Interstellar', 51), sep='\n')