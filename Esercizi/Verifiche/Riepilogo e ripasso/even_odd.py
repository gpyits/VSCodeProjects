# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    return {'pari':[i for i in lista if i%2==0], 'dispari': [i for i in lista if i%2!=0]}