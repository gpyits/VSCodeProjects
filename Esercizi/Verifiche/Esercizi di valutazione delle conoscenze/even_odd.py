# Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. 
# Restituisce l'elenco riorganizzato.

def even_odd_pattern(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda x: x%2)

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))