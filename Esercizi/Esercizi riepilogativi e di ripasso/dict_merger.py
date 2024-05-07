# Scrivi una funzione che unisce due dizionari. 
# Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    result={k:v for k, v in dict1.items()}
    for k in dict2.keys():
        try: 
            result[k]=dict1[k]+dict2[k]
        except KeyError:
            result[k]=dict2[k]
    return result

print(merge_dictionaries({'x': 5}, {'x': -5})) #{'x': 0}