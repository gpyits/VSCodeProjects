# Hai il compito di indagare su un caso di numeri mancanti! 
# Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, dove n è la lunghezza dell'elenco. 
# Sembra però che ci sia un problema: mancano alcuni numeri!

# La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti. 
# Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.

# La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale. 

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    return [i for i in range(min(nums), max(nums)) if i<=len(nums) and i not in nums]

print(find_disappeared_numbers([1,8,9,150]))