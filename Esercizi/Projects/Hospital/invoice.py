#### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.
#
# - Definire i seguenti metodi:
#
#     init(patients, doctor): 
#       Deve avere come input una lista di pazienti ed un dottore. 
#       Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). 
#       In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int). 
#       In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come ad esempio: 
#       "Non è possibile creare la classe fattura poichè il dottore non è valido!".
#
#     getSalary(): 
#       Deve ritornare il salario guadagnato dal dottore. 
#       Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
#
#     getBills(): 
#       Deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
#
#     addPatient(newPatient):
#       Consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
#       richiamando il metodo getBills() e getSalary(). 
#       Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
#
#     removePatient(): 
#       Consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, 
#       aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
#       Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
from doctor import Doctor
from patient import Patient

class Invoice:
    def __init__(self, doctor: Doctor) -> None:
        self.doctor: Doctor=doctor if doctor.isAValidDoctor() else None
        self.patients: list[Patient]=[] if doctor.isAValidDoctor() else None
        self.bills: int=len(self.patients) if doctor.isAValidDoctor() else None
        self.salary: int=0 if doctor.isAValidDoctor() else None
        if not self.doctor: print('Unable to create class Invoice: invalid doctor')
    def getSalary(self) -> float:
        self.salary=self.doctor.getParcel()*self.bills; return self.salary
    def getBills(self) -> int:
        self.bills: int=len(self.patients); return self.bills
    def addPatient(self, patient: Patient) -> None:
        if patient not in self.patients: 
            self.patients.append(patient), print(f'Patient {patient.getidCode()} was added to doctor {self.doctor.getName()} {self.doctor.getLastName()}\'s patients list')
            self.getSalary(), self.getBills()
        else: raise ValueError('Patient is already in patients list')
    def removePatient(self, patient: Patient):
        if patient in self.patients: 
            self.patients.remove(patient), print(f'Patient {patient.getidCode()} was removed from doctor {self.doctor.getName()} {self.doctor.getLastName()}\'s patients list')
            self.getSalary(), self.getBills()
        else: raise ValueError('Patient was not found')