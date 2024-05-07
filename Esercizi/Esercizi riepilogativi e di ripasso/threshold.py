# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

#slightly faster version than the one I submitted
def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    result=[]
    for i in sorted(numbers, reverse=True):
        if i>threshold:
            result.append(i)
        else:
            return sum(result)

print(sum_above_threshold([15, 5, 25], 20)) #expected 25