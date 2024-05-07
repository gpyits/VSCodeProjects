# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

def list_statistics(numbers: list[int]) -> tuple:
    return (max(numbers), min(numbers), sum(numbers)/len(numbers))

print(list_statistics([1, 2, 3, 4, 5])) #expected (5, 1, 3.0)