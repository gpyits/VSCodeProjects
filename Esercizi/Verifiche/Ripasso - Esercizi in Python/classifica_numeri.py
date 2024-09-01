# Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi.
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    return {'positivi':[i for i in lista if i*-1<i], 'negativi':[i for i in lista if i*-1>i]}