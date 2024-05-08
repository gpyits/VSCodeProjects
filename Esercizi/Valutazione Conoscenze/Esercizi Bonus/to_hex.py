# Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale. 
# Per gli interi negativi viene utilizzato il metodo del complemento a due.
# Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.
# Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

#extremely inefficient
def to_bin(num: int):
    is_negative=True if num*-1==abs(num) else False
    num=abs(num)
    result=[]
    while num>1:
        result.append(num%2)
        num//=2
    else:
        result.append(1)
        if is_negative==False:
            return (result), is_negative
        else:
            complement=[]
            for i in result[::-1]:
                complement.append(1 if i==0 else 0)
            result=[]
            one=[0 for i in complement[1:]]+[1]
            overflow=0
            for r in range(len(complement)-1, 0, -1):
                result.append(bin_sum(complement[r], one[r], overflow)[0])
                overflow=bin_sum(complement[r], one[r], overflow)[1]
            result.append(bin_sum(complement[0], overflow)[0])
            if bin_sum(complement[0], overflow)[1]==1:
                result.append(1)
            return result[::-1], is_negative

#change how this works to carry last overflow inside, maybe changing it to add the whole number instead of just two bits
def bin_sum(num1, num2, overflow=0):
    if overflow==0:
        if num1+num2==2:
            return 0, 1
        elif num1+num2==1:
            return 1, 0
        else:
            return 0, 0
    else:
        if num1+num2==2:
            return 1, 1
        elif num1+num2==1:
            return 0, 1
        else:
            return 1, 0

#condense for loops
def to_hex(num: int) -> str:
    conversion_table={'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', '1000':'8', '1001':'9',
                      '1010':'a', '1011':'b', '1100':'c', '1101':'d', '1110':'e', '1111':'f'}
    is_negative=to_bin(num)[1]
    num=to_bin(num)[0]
    for r in range(16-len(num)):
        num.append(1 if is_negative else 0)
    num=num[::-1]
    result=[]
    for r in range(4):
        result.append(conversion_table[''.join(str(i) for i in num[:4])])
        del num[:4]
    result2=''.join(i for i in result)
    while result2[0]=='0':
        result2=result2[1:]
    #what's the point of 2's comp then? find out what this should be actually returning
    return '0x'+result2 if is_negative==False else '-0x'+result2

print(to_hex(10))
print(to_bin(-10))