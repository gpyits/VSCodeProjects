#Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

def countdown(n: int) -> int:
    for r in range(n, -1, -1):
        print(r)

countdown(5)