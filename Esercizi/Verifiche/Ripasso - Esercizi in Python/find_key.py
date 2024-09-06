# Scrivi una funzione che prenda un dizionario e un valore, e ritorni una lista con tutte le chiavi che corrispondono a quel valore, o una lista vuota se il valore non è presente.
def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
    return [i for i in dizionario if dizionario[i]==valore]