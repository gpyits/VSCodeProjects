#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

def remove_duplicates(input_list: list[int, str]) -> list:
    return sorted(list(set(input_list)), key=lambda x: input_list.index(x))

print(remove_duplicates([4, 5, 'a', 4, 6])) #expected [4, 5, 'a', 6]