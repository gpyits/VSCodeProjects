# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario 
# con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    return {k:v-v*10/100 for k, v in prodotti.items() if v>20}

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))