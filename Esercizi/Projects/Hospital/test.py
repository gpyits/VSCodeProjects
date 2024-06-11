#### Creazione di Test Case con UnitTest
#
# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. 
# I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
#
# -Istruzioni:
# Creare un nuovo file Python denominato "test_persona.py".
# Importare il modulo unittest e tutte le classi definite.
#
# Test della Classe Persona
# - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi first_name, last_name e age.
#   - Il funzionamento dei metodi setName, setLastName e setAge.
#
# Test della Classe Dottore
# - Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Dottore.
#   - Il funzionamento del metodo isValidDoctor con diverse età.
#
# Test della Classe Paziente
# - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Paziente.
#
# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta della classe Fattura.
#   - Il calcolo corretto del salario e del numero di fatture.
#   - L'aggiunta e la rimozione di pazienti dalla lista.
import unittest
from hospital import *

class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person=Person('Luigi', 'Mario')
        self.person.setAge(24)
        self.none=Person(0, 0)
    def test_person(self) -> None:
        #verify init
        self.assertEqual(self.person.getName(), 'Luigi')
        self.assertEqual(self.person.getLastName(), 'Mario')
        self.assertEqual(self.person.getAge(), 24)
        #verify set
        self.person.setName('Koopa')
        self.person.setLastName('Troopa')
        self.assertEqual(self.person.getName(), 'Koopa')
        self.assertEqual(self.person.getLastName(), 'Troopa')
        #errors
        self.assertEqual((self.none.getName(), self.none.getLastName(), self.none.getAge()), (None, None, None))
        self.assertEqual(self.none.setName(0), 'First name must be a string')
        self.assertEqual(self.none.setLastName(0), 'Last name must be a string')
        self.assertEqual(self.none.setAge(-6), 'Age must be a positive integer')
        #greet
        self.person.greet()

class TestDoctor(unittest.TestCase):
    def setUp(self) -> None:
        self.doctor=Doctor('Bowser', 'Jr', 'Coroner', 50.0)
        self.none=Doctor(None, None, 0, 5)
        self.none.setAge(0)
        self.doctor.setAge(30)
    def test_doctor(self) -> None:
        #verify init
        self.assertEqual(self.doctor.getSpecialization(), 'Coroner')
        self.assertEqual(self.doctor.getParcel(), 50.0)
        #verify set
        self.doctor.setSpecialization('GP')
        self.doctor.setParcel(40.0)
        self.assertEqual(self.doctor.getSpecialization(), 'GP')
        self.assertEqual(self.doctor.getParcel(), 40.0)
        #errors
        self.assertEqual((self.none.getSpecialization(), self.none.getParcel()), (None, None))
        self.assertEqual(self.doctor.setSpecialization(0), 'Specialization must be a string')
        self.assertEqual(self.doctor.setParcel('12.5'), 'Parcel must be a float')
        #class sspecific methods
        self.assertEqual(self.doctor.isAValidDoctor(), True)
        self.assertEqual(self.none.isAValidDoctor(), False)
        #greet
        self.doctor.doctorGreet()

class TestPatient(unittest.TestCase):
    def setUp(self) -> None:
        self.patient=Patient('Morton', 'Koopa', 'wrld6')
        self.none=Patient(None, None, None) #put init error like all the other classes?
    def test_patient(self) -> None:
        #verify init
        self.assertEqual(self.patient.getidCode(), 'wrld6')
        #verify set
        self.patient.setIdCode('wrld7')
        self.assertEqual(self.patient.getidCode(), 'wrld7')
        #errors
        self.assertIsNone(self.none.getidCode())
        self.assertEqual(self.patient.setIdCode(7), 'ID must be a string')
        #patient info
        self.patient.patientInfo()

# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta della classe Fattura.
#   - Il calcolo corretto del salario e del numero di fatture.
#   - L'aggiunta e la rimozione di pazienti dalla lista.
class TestInvoice(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def test_invoice(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()