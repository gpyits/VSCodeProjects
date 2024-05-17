# Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
# Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.

# La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
# Non utilizzare nessuna funzione della libreria math!

def integerPower(base: int, exponent: int) -> int:
    x=base
    for i in range(exponent-1):
        base*=x
    return base

print(integerPower(5, 3)) #125