# Si vuole progettare un sistema in Python per la gestione delle prenotazioni alberghiere. Il sistema dovrà gestire diverse tipologie di camere, tra cui camere standard e suite.
#  
# 1. Classe astratta Camera
# Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di camera, 
# come il numero della camera (stringa) e la capacità massima di ospiti (numero intero) che sono attributi passati come argomenti in input. 
# Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; 
# il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
#  
# Metodi:
#     si definisca il metodo astratto prenota_camera().
#     si definisca il metodo astratto posti_disponibili().

# 2. Classe CameraStandard
# Estende la classe Camera e definisce gli attributi numero della camera e capacità massima di ospiti. Il costruttore deve inoltre gestire l'attributo numero_ospiti, il quale consente di stabilire quanti ospiti sono stati riservati per la camera. Il costruttore non deve ricevere in input questo argomento, ma assegnare loro un valore iniziale pari a 0.
#  
# Metodi:
#     posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali nella camera nel seguente modo: il dizionario deve avere due chiavi, ovvero, 'posti disponibili' e 'numero_ospiti'. Alla chiave 'posti disponibili' associare come rispettivo valore il numero di posti disponibili rimasti nella camera, alla chiave 'numero_ospiti' associare come rispettivo valore il numero di ospiti che sono rimasti disponibili nella camera. Se i posti disponibili nella camera sono esauriti, il valore da associare alla corrispondente chiave è 0.
#     prenota_camera(ospiti): che consente di prenotare un certo numero di ospiti per la camera. Tale metodo, prima di riservare la camera, deve controllare che ci siano posti disponibili per la tipologia di camera. In caso affermativo, contare il numero degli ospiti prenotati. Inoltre, nel caso in cui sia possibile prenotare la camera, il metodo deve stampare a schermo un messaggio che notifichi all'utente di aver riservato un tot di posti nella camera (specificando il numero della camera). In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella camera. Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Camera, sommando il numero di prenotazioni ricevute.

#  
# Classe Suite
# Estende la classe Camera e definisce gli attributi numero della camera e capacità massima di ospiti. Il costruttore deve inoltre gestire il costo della camera (numero float) per la suite. Una suite è una camera di cui tutti i posti disponibili vengono acquistati tutti insieme in una sola volta.
#  
# Metodi:

#     prenota_camera(): questo metodo verifica che se la camera è vuota, ovvero i posti disponibili sono pari alla capacità massima di ospiti. In quel caso, è possibile prenotare un numero di posti pari alla capacità massima di posti supportata dalla suite. Nel caso in cui la prenotazione suite andasse a buon fine, il metodo deve stampare a schermo un messaggio in cui avvisa l'utente che la suite (specificandone il numero della camera) è stata prenotata completamente, mostrando anche il prezzo pagato. In caso contrario, il metodo deve mostrare un messaggio a schermo in cui avvisa l'utente che la suite è già prenotata.
#     posti_disponibili(): che ritorna il numero di posti disponibili totali nella suite.

# Classe Hotel
# Questa classe deve avere un costruttore che richiede come argomento in input solo il nome dell'hotel (stringa) ed il prezzo standard di una camera (numero float), e creare una lista vuota chiamata stanze. La classe Hotel deve gestire molteplici camere standard e suite, attraverso i seguenti metodi:

#     aggiungi_camera(camera): la camera deve essere aggiunta alla lista delle stanze dell'hotel.
#     rimuovi_camera(camera): la camera deve essere rimossa dalla lista delle stanze dell'hotel.
#     mostra_stanze(): tale metodo deve stampare a schermo tutte le camere che fanno parte dell'hotel, specificando il numero di ogni camera.
#     guadagno(): questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali) il guadagno ricavato dalla vendita delle camere nell'hotel. Su ogni camera della lista, il prezzo per una camera standard è pari al prezzo standard, mentre il prezzo per una suite vale il doppio del prezzo standard.

# Test con codice driver
# Scrivere un codice driver che consenta di creare camere standard e suite in un hotel.
# Per la camera standard eseguire i seguenti passaggi:

#     Mostrare su schermo tutti i posti disponibili nella camera.
#     Provare a prenotare un numero di posti, esaurendo i posti disponibili nella camera (capacità massima).
#     Effettuare un altro tentativo di prenotazione. Questa volta, la prenotazione non dovrebbe andare a buon fine in quanto la camera deve risultare completa.

# NOTA: Per ogni tentativo di prenotazione, stampare i posti disponibili rimasti nella camera standard.

# Per la suite eseguire i seguenti passaggi:

#     Stampare a schermo i posti disponibili nella suite.
#     Provare a prenotare tutta la suite.
#     Provare ad effettuare un secondo tentativo di prenotazione. In questo caso, la prenotazione dovrebbe fallire, in quanto la suite dovrebbe essere già prenotata.

# Successivamente, creare una seconda camera standard e provare a prenotare un numero di posti.
#  
# Infine, creare un hotel. Aggiungere le due camere standard e la suite all'hotel. Stampare le stanze dell'hotel. Calcolare il guadagno dell'hotel ricavato dalla vendita delle camere.
# NOTA: Scrivere l'output su terminale anche su un file chiamato report.txt


# 1. Classe astratta Camera
# Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di camera, 
# come il numero della camera (stringa) e la capacità massima di ospiti (numero intero) che sono attributi passati come argomenti in input. 
# Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; 
# il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
#  
# Metodi:
#     si definisca il metodo astratto prenota_camera().
#     si definisca il metodo astratto posti_disponibili().
class Camera:
    def __init__(self) -> None:
        pass