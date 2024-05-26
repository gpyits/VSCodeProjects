# Scrivi un programma in Python che gestisca un magazzino. 
# Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
#  
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
class Product:
    def __init__(self, name: str, quantity: int) -> None:
        self.name: str=name
        self.quantity: int=quantity
    
class Warehouse:
    def __init__(self, products: list[Product]) -> None:
        self.products: list[Product]=products
    def add_product(self, product: Product) -> None:
        self.products.append(product)
    def cerca_prodotto(self, product_name: str) -> Product:
        for product in self.products:
            if product.name==product_name:
                return product
    def verify_availability(self, product_name:str) -> bool:
        for product in self.products:
            if product.name==product_name:
                return True if product.quantity>0 else False