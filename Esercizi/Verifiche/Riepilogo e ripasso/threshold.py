# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    return sum([i for i in numbers if i>threshold])