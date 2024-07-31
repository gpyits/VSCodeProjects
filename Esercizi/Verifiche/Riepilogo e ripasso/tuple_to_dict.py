# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    result={}
    for i in tuples:
        if i[0] not in result:
            result[i[0]]=[i[1]]
        else:
            result[i[0]].append(i[1])
    return result