# Data una stringa s e una lista di stringhe wordDict, 
# restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.
# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
def word_break(s: str, wordDict: list[str]) -> bool:
    wordDict={i:r for i, r in zip([i for i in range(len(wordDict))], [r for r in wordDict])}
    useful_words=sorted([word for word in set(wordDict.values()) if word in s], key=lambda x: s.index(x))
    useful_substrings=[]
    for i in range(len(useful_words)):
        substring=''
        for word in useful_words[i:]:
            if substring+word in s:
                substring+=word
            else:
                continue
        useful_substrings.append(substring)
    return max(useful_substrings, key=len) in s if len(''.join(string for string in wordDict.values()))<len(s) else s in useful_substrings

print(word_break("leetcode", ["leet","code"])) #True
print(word_break("catsandog",["cats","dog","sand","and","cat"])) #False