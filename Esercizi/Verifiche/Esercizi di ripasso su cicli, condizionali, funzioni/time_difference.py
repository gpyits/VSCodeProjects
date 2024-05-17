# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) 
# e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
# (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).
# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. 
# La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, 
# entrambi contenuti entro un ciclo dell'orologio di 12 ore.
# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

def seconds_since_noon(hours: int, minutes: int, seconds: int) -> int:
    return (hours*3600)+(minutes*60)+seconds if hours<12 and hours!=0 else ((hours-12)*3600)+(minutes*60)+seconds

def time_difference(hours_1: int, minutes_1: int, seconds_1: int, hours_2: int, minutes_2: int, seconds_2: int) -> int:
    return abs(seconds_since_noon(hours_1, minutes_1, seconds_1)-seconds_since_noon(hours_2, minutes_2, seconds_2))

print(time_difference(1, 0, 0, 3, 15, 30)) #8130