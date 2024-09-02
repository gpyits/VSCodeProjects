# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for k in dict2:
        if k in dict1:
            dict1[k]=dict1[k]+dict2[k]
        else:
            dict1[k]=dict2[k]
    return dict1