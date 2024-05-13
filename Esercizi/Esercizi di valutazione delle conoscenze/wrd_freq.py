# Scrivi una funzione che accetta una stringa come input, 
# rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente 
# (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    words={}
    for word in text.split():
        word=word.lower()
        while ord(word[-1]) in list(range(32, 47))+list(range(57, 64)): word=word[:-1]
        if word not in stopwords:
            if word in words:
                words[word]+=1
            else:
                words[word]=1
    return words

print(word_frequency(text, stopwords))