# Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). 
# Questi gioielli hanno vari valori, alcuni più preziosi di altri. 
# Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.

# Qual è la svolta?
# Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). 
# A noi però interessano solo valori distinti, ovvero gioielli con valori unici.

# Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). 
# Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.

# Ma c'è un problema!
# Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(nums: list[int]) -> int:
    dupes={}
    final_nums=[]
    for number in nums:
        if number in dupes:
            dupes[number]+=1
        else:
            dupes[number]=1
    if min(dupes.values())==max(dupes.values()) and len(dupes.values())==2:
        return max(nums)
    else:
        minimum_dupe=min(dupes.values())
        for number in dupes:
            if dupes[number]==minimum_dupe:
                final_nums.append(number)
        if len(final_nums)<=2:
            return min(final_nums)
        else:
            return final_nums[2]

print(third_max([3, 2, 1])) #expected 1