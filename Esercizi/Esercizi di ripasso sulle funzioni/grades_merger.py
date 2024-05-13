# Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    result={person['nome']:[] for person in voti}
    for person in voti:
        if person['nome'] in result:
            result[person['nome']].append(person['voto'])
    return result

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))