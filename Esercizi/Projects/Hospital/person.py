#### CLASSE: Persona
#
# Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. 
# Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
# - La classe Persona deve avere i seguenti metodi:
#
#     init(first_name, last_name):
#       Tale metodo, deve verificare che first_name, last_name siano stringhe.
#       In caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio: "Il nome inserito non è una stringa!". 
#       Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una person. 
#       Se first_name e last_name non sono due stringhe, allora assegnare None all'età.
#
#     setName(first_name):
#       Consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
#       Il valore viene modificato se e solo se viene passata al metodo una stringa. 
#       In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
#
#     setLastName(last_name): 
#       Consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
#       Il valore viene modificato se e solo se viene passata al metodo una stringa. 
#       In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
#
#     setAge(age): 
#       Consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
#       Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
#       In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
#
#     getName(): 
#       Consente di ritornare il nome di una persona.
#
#     getLastname(): 
#       Consente di ritornare il cognome di una persona.
#
#     getAge(): 
#       Consente di ritornare l'età di una persona.
#
#     greet(): 
#       Stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"

class Person:
  def __init__(self, first_name: str, last_name: str) -> None:
    self.__first_name: str=first_name if type(first_name)==str else print('First name must be a string')
    self.__last_name: str=last_name if type(last_name)==str else print('Last name must be a string')
    self.__age: int=0 if self.__first_name and self.__last_name else None
  def setName(self, first_name: str) -> None:
    if type(first_name)!=str: print('First name must be a string'); return
    self.__first_name: str=first_name
  def setLastName(self, last_name: str) -> None:
    if type(last_name)!=str: print('Last name must be a string'); return
    self.__last_name: str=last_name
  def setAge(self, age: int) -> None:
    if type(age)!=int: print('Age must be an integer'); return
    self.__age: int=age
  def getName(self) -> str:
    return self.__first_name
  def getLastName(self) -> str:
    return self.__last_name
  def getAge(self) -> int:
    return self.__age
  def greet(self) -> None:
    print(f'Hi, my name is {self.getName()} {self.getLastName()}! I am {self.getAge()} years old!')