# Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine e false in caso contrario. 
# Ogni lettera nella magazine può essere utilizzata solo una volta in note.

def ransom(note: str, magazine: str) -> bool:
    note=[i for i in note]
    magazine=[i for i in magazine]
    result=[]
    for i in note:
        if i in magazine:
            magazine.pop(magazine.index(i))
            result+=i
    if result==note:
        return True
    else:
        return False

print(ransom("aa","aab"))