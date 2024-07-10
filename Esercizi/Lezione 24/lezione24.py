# Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
# Si crei un metodo getText() che restituisca il testo. 
# Si crei un metodo setText() per impostare il testo. 
# Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.
#
# Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
# Si implementino i metodi get() e set() appropriati per tali variabili. 
# Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
# Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
#       Da: alice@example.com, A: bob@example.com
#       Titolo: Incontro
#       Messaggio: Ciao Bob, possiamo incontrarci domani?
# Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
#  
# Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
# Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
# I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso 
# e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
# Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:ù
#       Percorso: nomePercorso/document.txt
#       Contenuto: Questo e' il contenuto del file.
class Documento:
    def __init__(self) -> None:
        self.__text: str
    def setText(self, text: str) -> None:
        self.__text=text
    def getText(self) -> str:
        return self.__text
    def isInText(self, word: str) -> bool:
        return word in self.__text
    
class Email(Documento):
    def __init__(self) -> None:
        self.__mittente: str
        self.__destinatario: str
        self.__titolo: str
    def setMittente(self, mittente: str) -> None:
        self.__mittente=mittente
    def setDestinatario(self, destinatario) -> None:
        self.__destinatario=destinatario
    def setOggetto(self, oggetto) -> None:
        self.__oggetto=oggetto
    def getMittente(self) -> str:
        return self.__mittente
    def getDestinatario(self) -> str:
        return self.__destinatario
    def getTitolo(self) -> str:
        return self.__titolo
    def getText(self) -> str:
        return f'Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo()}\nMessaggio: {super().getText()}'
    def writeToFile(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self.getText())

class File(Documento):
    def __init__(self, nomePercorso: str) -> None:
        self.nomePercorso: str
    def leggiTestoDaFile(self) -> str:
        with open(self.__nomePercorso, 'r') as file:
            self.__testo=file.read()
    def getText(self) -> str:
        return f'Percorso: {self.nomePercorso}\nContenuto: {super().getText()}'
    
# ### Test tramite codice driver:
# Creazione degli oggetti:
#     Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
#     File: Viene creato un oggetto File specificando il percorso di un file esistente.
#
# Prova dei metodi:
#     Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
#     Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().
#
# Scrittura del contenuto dell'email su un file:
#     Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt utilizzando il metodo writeToFile().
#
# Verifica della presenza di parole chiave:
#     Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email. Il risultato atteso è True.
#     File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file. Il risultato atteso è False.
