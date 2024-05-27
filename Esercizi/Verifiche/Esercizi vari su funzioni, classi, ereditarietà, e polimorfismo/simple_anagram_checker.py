# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
# in genere utilizzando tutte le lettere originali esattamente una volta.
def anagram(s: str, t: str) -> bool:
    return sorted(s.lower())==sorted(t.lower())

print(anagram("anagram","nagaram")) #True