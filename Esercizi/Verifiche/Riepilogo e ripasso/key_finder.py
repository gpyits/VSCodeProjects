#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    try: 
        for k, v in dizionario.items():
            if v == valore:
                return k
    except KeyError:
        return None