# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di elettrodomestici.

# 1. Classe Base: Elettrodomestico
# Crea una classe base chiamata Elettrodomestico con i seguenti attributi e metodi:
#  
# Attributi:
#     marca: str
#     modello: str
#     potenza: int
# Metodi:
#     __init__(self, marca: str, modello: str, potenza: int): metodo costruttore che inizializza gli attributi marca, modello e potenza.
#     descrivi_elettrodomestico(self): metodo che stampa una descrizione dell'elettrodomestico nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W"

# 2. Classe Derivata: Frigorifero
# Crea una classe derivata chiamata Frigorifero che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:
# Attributi:
#     capacità: int
# Metodi:
#     __init__(self, marca: str, modello: str, potenza: int, capacità: int): metodo costruttore che inizializza gli attributi della classe base e capacità.
#     descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche la capacità nella descrizione, 
#                                      nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W, Capacità: {capacità}L"

# 3. Classe Derivata: Lavatrice
# Crea una classe derivata chiamata Lavatrice che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:
# Attributi:
# - carico_max: int
# Metodi:
# - __init__(self, marca: str, modello: str, potenza: int, carico_max: int): metodo costruttore che inizializza gli attributi della classe base e carico_max.
# - descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche il carico massimo nella descrizione, 
#                                    nel formato "Marca: {self.marca}, Modello: {modello}, Potenza: {potenza}W, Carico massimo: {carico_max}kg".
class Elettrodomestico:
    def __init__(self, marca: str, modello: str, potenza: int) -> None:
        self.marca: str=marca
        self.modello: str=modello
        self.potenza: int=potenza
    def descrivi_elettrodomestico(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W")

class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, capacità: int) -> None:
        super().__init__(marca, modello, potenza)
        self.capacità: int=capacità
    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L")

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, carico_max: int) -> None:
        super().__init__(marca, modello, potenza)
        self.carico_max: int=carico_max
    def descrivi_elettrodomestico(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg")