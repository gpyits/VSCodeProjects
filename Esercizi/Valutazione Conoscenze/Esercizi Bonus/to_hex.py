# Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale. 
# Per gli interi negativi viene utilizzato il metodo del complemento a due.
# Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.
# Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

def to_bin(num: int):
    is_negative=True if num*-1==abs(num) else False
    num=abs(num)
    result=''
    while num>1:
        result+=str(num%2)
        num//=2
    else:
        result+='1'
        if is_negative==False:
            return (result)[::-1]
        else:
            complement=''
            for i in result[::-1]:
                complement+='1' if i=='0' else '0'
            return bin_sum(result, complement)


def bin_sum(num1, num2):
    result=''

    return result

def to_hex(num: int) -> str:
    num=to_bin(num)
    pass

print(bin_sum('00', '01')) #expected 01
print(to_bin(-4))