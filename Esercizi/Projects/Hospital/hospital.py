'''
### CLASSE: Persona

Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. 
Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
- La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name):
      Tale metodo, deve verificare che first_name, last_name siano stringhe.
      In caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio: "Il nome inserito non è una stringa!". 
      Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una person. 
      Se first_name e last_name non sono due stringhe, allora assegnare None all'età.

    setName(first_name):
      Consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
      Il valore viene modificato se e solo se viene passata al metodo una stringa. 
      In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
    
    setLastName(last_name): 
      Consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
      Il valore viene modificato se e solo se viene passata al metodo una stringa. 
      In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

    setAge(age): 
      Consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
      Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
      In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

    getName(): 
      Consente di ritornare il nome di una persona.

    getLastname(): 
      Consente di ritornare il cognome di una persona.

    getAge(): 
      Consente di ritornare l'età di una persona.

    greet(): 
      Stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"

### CLASSE Dottore
Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float). Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:

    __init__(self): 
      Costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). 
      Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".

    setSpecialization(specialization): 
      Consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. 
      Il valore viene modificato se e solo se viene passata al metodo una stringa. 
      In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

    setParcel(parcel): 
      Consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. 
      Il valore viene modificato se e solo se viene passato al metodo un float. 
      In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

    getSpecialization(): 
      Consente di ritornare la specializzazione del dottore.

    getParcel(): 
      Consente di ritornare la parcella del dottore.

    isAValidDoctor(): 
      Stabilisce se un dottore è un dottore valid: 
      Un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. 
      Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. 
      In caso contrario, stampare "Doctor nome e cognome is not valid!".

    doctorGreet():
      Tale metodo richiama la funzione greet() della classe Persona. 
      Poi, stampa il seguente saluto "Sono un medico {specializzazione}"

### CLASSE: Paziente
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    __init__(self): 
      Costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.

    setIdCode(idCode): 
      Consente di impostare il codice identificativo del paziente.

    getidCode(): 
      Consente di ritornare il codice identificativo del paziente.

    patientInfo(): 
      Stampa in output le informazioni del paziente in questo modo:
        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"

### CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor): 
      Deve avere come input una lista di pazienti ed un dottore. 
      Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). 
      In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int). 
      In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come ad esempio: 
      "Non è possibile creare la classe fattura poichè il dottore non è valido!".

    getSalary(): 
      Deve ritornare il salario guadagnato dal dottore. 
      Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
    
    getFatture(): 
      Deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
    
    addPatient(newPatient): 
      Consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
      richiamando il metodo getFatture() e getSalary(). 
      Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
    
    removePatient(): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

### Creazione di Test Case con UnitTest

Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.

-Istruzioni:
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Persona
- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi first_name, last_name e age.
  - Il funzionamento dei metodi setName, setLastName e setAge.

Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età.

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.
'''
