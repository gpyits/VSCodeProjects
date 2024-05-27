# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

#     Classe Book:
#         Attributi:
#             book_id: str - Identificatore di un libro.
#             title: str - titolo del libro.
#             author: str - autore del libro
#             is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#         Metodi:
#             borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#             return_book()- Contrassegna il libro come restituito.

#     Classe Member:
#         Attributi:
#             member_id: str - identificativo del membro.
#             name: str - il nome del membro.
#             borrowed_books: list[Book] - lista dei libri presi in prestito.
#         Metodi:
#             borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#             return_book(book): rimuove il libro dalla lista borrowed_books.

#     Classe Library:
#         Attributi:
#             books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#             members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#         Metodi:
#             add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#             register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#             borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#             return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#             get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool=False) -> None:
        self.book_id: str=book_id
        self.id: str=title
        self.author: str=author
        self.is_borrowed: bool=is_borrowed
    def borrow(self) -> None:
        self.is_borrowed=True
    def return_book(self) -> None:
        self.is_borrowed=False

class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]=[]) -> None:
        self.id: str=member_id
        self.name: str=name
        self.borrowed_books: list[Book]=borrowed_books
    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)
        book.is_borrowed=True
    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)
        book.is_borrowed=False

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book]=[]
        self.members: dict[str, Member]=[]
    def add_book(self, book_id: str, title: str, author: str) -> None:
        self.books.append(Book(book_id, title, author))
    def register_member(self, member_id:str, name: str) -> None:
        self.members.append(Member(member_id, name))


    def borrow_book(self, member_id: str, book_id: str) -> None:
        member=[member for member in self.members if member.id==member_id]
        book=[book for book in self.books if book.id==book_id]
        if member==[]: print('Membro non trovato')
        if book==[]: print('Libro non trovato')
        ##############


    def return_book(self, member_id: str, book_id: str) -> None:
        [member for member in self.members if member.id==member_id][0].return_book([book for book in self.books if book.id==book_id][0])
    def get_borrowed_books(self, member_id: str) -> list[Book]:
        return [member for member in self.members if member.id==member_id][0].borrowed_books
    
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']