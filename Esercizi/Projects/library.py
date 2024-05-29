# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
#     Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo: str=titolo
        self.autore: str=autore
        self.prestato=False

class Biblioteca:
    def __init__(self) -> None:
        self.libri: list[Libro]=[]
    def aggiungi_libro(self, libro: Libro) -> str:
        self.libri.append(libro)
        return 'Libro aggiunto'
    def presta_libro(self, libro: Libro) -> str:
        libro.prestato=True
        return 'Libro prestato'
    def restituisci_libro(self, libro: Libro) -> str:
        libro.prestato=False
        return 'Libro restituito'
    def mostra_libri_disponibili(self) -> list[str]:
        libri_disponibili: list[Libro]=[libro.titolo for libro in self.libri if not libro.prestato]
        return libri_disponibili if libri_disponibili else 'Errore: nessun libro disponibile'
    
libro1=Libro('Lorem', 'Ipsum')
libro2=Libro('1984', 'George Orwell')
biblioteca=Biblioteca()
print(biblioteca.aggiungi_libro(libro1),\
      biblioteca.aggiungi_libro(libro2),\
      biblioteca.libri,\
      biblioteca.presta_libro(libro1),\
      biblioteca.mostra_libri_disponibili(),\
      biblioteca.restituisci_libro(libro1),\
      biblioteca.mostra_libri_disponibili(),\
      biblioteca.presta_libro(libro1),\
      biblioteca.presta_libro(libro2),\
      biblioteca.mostra_libri_disponibili(), sep='\n'
      )