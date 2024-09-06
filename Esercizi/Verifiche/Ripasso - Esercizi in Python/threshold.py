# Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un dato valore intero definito threshold.
def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    result=1
    numbers=[i for i in numbers if i<threshold]
    for number in numbers:
        result*=number
    return result