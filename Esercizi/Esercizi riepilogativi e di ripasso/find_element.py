# La funzione dovrebbe determinare se un elemento è presente in una lista.
# Un errore nell'implementazione porta a risultati inaspettati.

#sbagliata
def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        return False
    
#giusta
def find_element(lst: list[int], element: int) -> bool:
    if element in lst:
        return True
    else: 
        return False