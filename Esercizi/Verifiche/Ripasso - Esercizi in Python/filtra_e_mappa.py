# Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e restituisca un 
# nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    return {k:round(v+v*10/100, 2) for k, v in prodotti.items() if v<50}

print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0}))