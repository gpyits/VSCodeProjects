# Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
# La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. 
# Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

#very inefficient, I'll think of something else later
def rotate_left(elements: list, k: int) -> list:
    if k==0:
        return elements
    else:
        result=[elements[r+1] for r in range(len(elements)-1)]
        return rotate_left(result+[elements[0]], k-1)

print(rotate_left([1, 2, 3, 4, 5], 2)) #expected [3, 4, 5, 1, 2]