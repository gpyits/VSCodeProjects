# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
# restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    return {k:v-v*0.1 for k, v in prodotti.items() if v>20}