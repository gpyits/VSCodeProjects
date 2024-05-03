# Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. 
# Queste note possono avere altezze (valori) diversi. 
# Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la nota massimale e quella minimale è uguale a 1. 
# Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.

# Trovare l'armonia perfetta:
# Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). 
# La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. 
# Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

# Colpire le note giuste:
# Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
# La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

def find_lhs(nums: list[int]) -> int:
    sequences=[]
    for i in nums:
        sequence=[]
        for j in nums:
            if j==i+1 or j==i:
                sequence.append(j)
        sequences.append(sequence)
    return max([len(i) for i in sequences])

print(find_lhs([1, 3, 2, 2, 5, 2, 3, 7])) #5
print(find_lhs([1,1,1,1,2,2,2,2])) #8
print(find_lhs([1,2,3,4])) #2