#Due None
#this proves percentage choices using random.coice() are accurate to normal distribution
import random
tortoise_moves=[3, 3, 3, 3, 3, 1, 1, 1, -6, -6]
hare_moves=[1, 1, 1, -2, -2, 0, 0, 9, 9, -12]
tprob=[]
hprob=[]
for i in range(101):
    tprob.append(str(random.sample(tortoise_moves, 1)[0]))
    hprob.append(str(random.sample(hare_moves, 1)[0]))
tcount={}
hcount={}
for i in tprob:
    if i in tcount:
        tcount[i]+=1
    else:
        tcount[i]=1

for i in hprob:
    if i in hcount:
        hcount[i]+=1
    else:
        hcount[i]=1
# print(tcount, '\n\n', hcount)
        

# In questo problema ricreerete la classica gara tra la tartaruga e la lepre.
# Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
# I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati.
# Ogni quadrato rappresenta una posizione lungo il percorso della corsa.
# Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara.
# Durante la corsa, i contendenti possono occasionalmente perdere terreno.
# C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

# - Tartaruga:
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

# Il percorso è rappresentato attraverso l'uso di una lista. 
# Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). 
# Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). 
# Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. 
# Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. 
# Usate una tecnica simile per muovere la lepre seguendo le sue regole.

# Iniziate la gara stampando:
# 'BANG !!!!! AND THEY'RE OFF !!!!!'

# Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), 
# stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, 
# la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. 
# Occasionalmente, i contendenti si troveranno sullo stesso quadrato. 
# In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. 
# Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

# Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. 
# Se è così, stampate il nome del vincitore e terminate la simulazione. 
# Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". 
# Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". 
# Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

########REQUISITI DEL CODICE########
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio. 
# Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.

########SFIDE AGGIUNTIVE########
# 1. Variabilità Ambientale:
# Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
# Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
# Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
#  
# Modificatori mossa:
# - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
# - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
#  
# 2. Energia o Stamina:
# Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica. 
# Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. 
# L'energia inziale per entrambi gli animali è 100.

# Nuove regole di movimento:
# - Tartaruga:
#     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia.
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energiza iniziale.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
import random, time

def tortoise_hare(path=['H-T']+['_' for i in range(70)]):
    tortoise_moves, hare_moves=[3, 3, 3, 3, 3, 1, 1, 1, -6, -6], [1, 1, 1, -2, -2, 0, 0, 9, 9, -12]
    tortoise_position, hare_position=0, 0
    print(f'BANG! AND THEY\'RE OFF!\n\n{path}')
    round=0
    while tortoise_position<70 and hare_position<70:
        round+=1
        path=['_' for i in range(71)]
        #time.sleep(1)
        move_tortoise, move_hare=random.sample(tortoise_moves, 1)[0], random.sample(hare_moves, 1)[0]
        tortoise_position+=move_tortoise if tortoise_position+move_tortoise>=0 else -tortoise_position
        hare_position+=move_hare if hare_position+move_hare>=0 else -hare_position
        if tortoise_position>=70 or hare_position>=70:
            break
        elif tortoise_position!=hare_position:
            path[tortoise_position], path[hare_position]='T', 'H'
        else:
            path[tortoise_position]='OUCH!'
        print(f'Round {round}:\n{path}\n\nTortoise moved: {move_tortoise}, Tortoise position: {tortoise_position+1}\nHare moved: {move_hare}, Hare position: {hare_position+1}\n')
    path=['_' for i in range(71)]
    if tortoise_position>=70:
        tortoise_position=70
        hare_position+=random.sample(hare_moves, 1)[0] if hare_position+random.sample(hare_moves, 1)[0]>=1 else -hare_position+1
        if hare_position>=70:
            path[-1]='H-T'
            print(f'Round {round+1}:\n{path}\n\nTortoise moved: {move_tortoise}, Tortoise position: {70}\nHare moved: {move_hare}, Hare position: {70}\n\nIT\'S A TIE!')
        else:
            path[-1], path[hare_position]='T', 'H'
            print(f'Round {round+1}:\n{path}\n\nTortoise moved: {move_tortoise}, Tortoise position: {70}\nHare moved: {move_hare}, Hare position: {hare_position+1}\n\nTORTOISE WINS! || YAY!')
    elif hare_position>=70:
        hare_position=70
        path[-1], path[tortoise_position]='H', 'T'
        print(f'Round {round+1}:\n{path}\n\nTortoise moved: {move_tortoise}, Tortoise position: {tortoise_position+1}\nHare moved: {move_hare}, Hare position: {70}\n\nHARE WINS || YUCK!')

tortoise_hare()