# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
def frequency_dict(elements: list) -> dict:
    return {k:elements.count(k) for k in elements}