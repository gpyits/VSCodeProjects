# Immaginiamo di avere un tipo speciale di sistema numerico in cui gli unici elementi costitutivi sono i numeri 2, 3 e 5. 
# Chiamiamo questi elementi costitutivi "fattori primi" perché non possono essere ulteriormente scomposti. 
# Un "numero brutto" in questo sistema è un numero costruito utilizzando solo questi fattori primi (2, 3 o 5). 
# Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto, ma 7 (che ha un fattore primo pari a 7) non lo è.

def ugly_number(num: int) -> bool:
    result=[]
    while num>1:
        if num%2==0:
            num//=2
        elif num%3==0:
            num//=3
        elif num%5==0:
            num//=5
        else:
            return False
    else:
        return True


print(ugly_number(6))  #expected True
print(ugly_number(14)) #expected False