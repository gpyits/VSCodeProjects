# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, somma il valore al valore già associato alla chiave.
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    result={}
    for i, j in tuples:
        if i in result:
            result[i]+=j
        else:
            result[i]=j
    return result

print(lista_a_dizionario([("a", 1), ("a", 2), ("a", 3)]))