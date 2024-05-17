# Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
# La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.
# Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

def hypotenuse(width: float, height: float) -> float:
    return (width**2+height**2)**0.5

print(hypotenuse(3.0, 4.0)) #5.0