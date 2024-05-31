# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
#       Attributi:
#           marca (stringa)
#           modello (stringa)
#           anno (intero)
#
#       Metodi:
#           __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
#           descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
#
# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi: 
#       Attributi:
#           numero_porte (intero)

#       Metodi:
#           __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte
#           descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, 
#                                   nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".
#
# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
#       Attributi:
#           tipo(stringa, ad esempio "sportiva", "cruiser", ecc.)

#       Metodi:
#           __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
#           descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
class Veicolo:
    pass
class Auto(Veicolo):
    pass
class Moto(Veicolo):
    pass

veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() 
auto.descrivi_veicolo()
moto.descrivi_veicolo()

#Expected:
# Marca: Generic, Modello: Model, Anno: 2020
# Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
# Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva