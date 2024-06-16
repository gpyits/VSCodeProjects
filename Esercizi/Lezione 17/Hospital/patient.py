#### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.
#
# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:
#
#     __init__(self): 
#       Costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
#
#     setIdCode(idCode): 
#       Consente di impostare il codice identificativo del paziente.
#
#     getidCode(): 
#       Consente di ritornare il codice identificativo del paziente.
#
#     patientInfo(): 
#       Stampa in output le informazioni del paziente in questo modo:
#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"
from person import Person

class Patient(Person):
    def __init__(self, first_name: str, last_name: str, id: str) -> None:
        super().__init__(first_name, last_name)
        self.__id: str=id
    def setIdCode(self, id: str) -> None:
        if type(id)!=str:print('ID must be a string'); return
        self.__id: str=id
    def getidCode(self) -> str:
        return self.__id
    def patientInfo(self) -> None:
        print(f'Patient: {self.getName()} {self.getLastName()}\nID: {self.getidCode()}')