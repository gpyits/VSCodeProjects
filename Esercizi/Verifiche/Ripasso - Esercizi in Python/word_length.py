# Scrivi una funzione che, data una lista di parole, ritorni un dizionario che mappa ogni parola alla sua lunghezza.
def mappa_parole_a_lunghezza(words: list) -> dict:
    return {word:len(word) for word in words}