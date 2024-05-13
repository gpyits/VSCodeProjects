# Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
# Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for number in lista:
        if number in da_rimuovere:
            if da_rimuovere[number]>=1: 
                del lista[lista.index(number)]
                da_rimuovere[number]-=1
            else:
                continue
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))