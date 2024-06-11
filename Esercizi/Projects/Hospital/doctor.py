#### CLASSE Dottore
# Creare un file chiamato "dottore.py".
# In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.
#
# Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico 
# Generale), ed una parcella per le visite in studio (si usi il tipo float). Gli attributi della classe dottore devono essere anch'essi privati.
#
# - Definire i seguenti metodi:
#
#     __init__(self): 
#       Costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). 
#       Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, 
#       altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".
#
#     setSpecialization(specialization): 
#       Consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. 
#       Il valore viene modificato se e solo se viene passata al metodo una stringa. 
#       In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".
#
#     setParcel(parcel): 
#       Consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. 
#       Il valore viene modificato se e solo se viene passato al metodo un float. 
#       In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".
#
#     getSpecialization(): 
#       Consente di ritornare la specializzazione del dottore.
#
#     getParcel(): 
#       Consente di ritornare la parcella del dottore.
#
#     isAValidDoctor(): 
#       Stabilisce se un dottore è un dottore valid: 
#       Un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. 
#       Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. 
#       In caso contrario, stampare "Doctor nome e cognome is not valid!".
#
#     doctorGreet():
#       Tale metodo richiama la funzione greet() della classe Persona. 
#       Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
from person import Person

class Doctor(Person):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.__specialization: str=specialization if type(specialization)==str else print('Specialization must be a string')
        self.__parcel: float=parcel if type(parcel)==float else print('Parcel must be a float')
    def setSpecialization(self, specialization: str) -> None:
        if type(specialization)!=str: return 'Specialization must be a string'
        self.__specialization: str=specialization
    def setParcel(self, parcel: float) -> None:
        if type(parcel)!=float: return 'Parcel must be a float'
        self.__parcel: float=parcel
    def getSpecialization(self) -> str:
        return self.__specialization
    def getParcel(self) -> float:
        return self.__parcel
    def isAValidDoctor(self) -> bool:
        print(f'Doctor {self.getName()} {self.getLastName()} is valid') if self.getAge()>=30 else print(f'Doctor {self.getName()} {self.getLastName()} is not valid')
        return True if self.getAge()>=30 else False
    def doctorGreet(self) -> None:
        self.greet(), print(f'\nI\'m a {self.getSpecialization()}')