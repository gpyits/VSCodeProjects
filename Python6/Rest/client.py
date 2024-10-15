import requests, json, sys

base_url = "http://127.0.0.1:8080"

def GetCredenziali():

    global username, password

    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    credenziali = {
        "username": username,
        "password": password
    }
    return credenziali

def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino


def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova piÃ¹ tardi.")

print("Benvenuti al Comune - sede locale")

print("\nImmettere le credenziali: ")

accesso_effettuato = 0
permessi = 0


while accesso_effettuato == 0:
    richiesta = GetCredenziali()
    login_url = base_url + "/login"
    try:
        risposta = requests.post(login_url, json=richiesta)
        dizionario_risposta = risposta.json()
        if dizionario_risposta["Esito"] == "000":
            accesso_effettuato = 1
            if dizionario_risposta["Privilegio"] == "w":
                permessi = 1
                
            else:
                permessi = 0
            
        else:
            print("Accesso non consentito")
    
    except:
        print("Errore di comunicazione con il server")
        accesso_effettuato = 0

if permessi == 1:
    
    iFlag = 0
    while iFlag==0:
        print("\nOperazioni disponibili:")
        print("1. Inserisci cittadino")
        print("2. Richiedi cittadino")
        print("3. Modifica cittadino")
        print("4. Elimina cittadino")
        print("5. Esci")


        try:
            iOper = int(input("Cosa vuoi fare? "))
        except ValueError:
            print("Inserisci un numero valido!")
            continue


        if iOper == 1:
            print("Aggiunta cittadino")
            api_url = base_url + "/add_cittadino"
            jsonDataRequest = GetDatiCittadino()
            EseguiOperazione(1, api_url, jsonDataRequest)

        # Richiesta dati cittadino
        elif iOper == 2:
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = GetCodicefiscale()
            EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'],None)

        elif iOper == 3:
            print("Modifica cittadino")
            api_url = base_url + "/update_cittadino"
            jsonDataRequest = GetDatiCittadino()
            EseguiOperazione(3, api_url, jsonDataRequest)


        elif iOper == 4:
            print("Eliminazione cittadino")
            api_url = base_url + "/elimina_cittadino"
            jsonDataRequest = GetCodicefiscale()
            EseguiOperazione(4, api_url, jsonDataRequest)

        elif iOper == 5:
            print("Buona giornata!")
            iFlag = 1

        else:
            print("Operazione non disponibile, riprova.")
else:
    
    iFlag = 0
    while iFlag==0:
        print("\nOperazioni disponibili:")
        print("1. Richiedi cittadino")
        print("2. Esci")


        try:
            iOper = int(input("Cosa vuoi fare? "))
        except ValueError:
            print("Inserisci un numero valido!")
            continue

        # Richiesta dati cittadino
        if iOper == 1:
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = GetCodicefiscale()
            EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'],None)

        elif iOper == 2:
            print("Buona giornata!")
            iFlag = 1

        else:
            print("Operazione non disponibile, riprova.")