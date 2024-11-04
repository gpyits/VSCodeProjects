import requests,json
import sys

base_url = "https://127.0.0.1:8080"
auth = False

def GetDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome ")
    dataN = input("Qual'è la data di nascita? ")
    codF = input("Qual'è il codice fiscale? ")
    datiCittadino = {codF:{"nome":nome, "cognome": cognome, "dataNascita":dataN}}
    return datiCittadino

def GetCittadino():
    return input("Inserisci il codice fiscale della persona richiesta ")

def UpdateCittadino():
    dati_da_modifcare = [None for _ in range(4)]
    dati_da_modifcare[0] = input("Inserisci il codice fiscale della persona a cui vuoi modificarei i dati")
    nome = input("Inserisci il nome modificato (Lascia vuoto per non cambiare) ")
    cognome = input("Inserisci il cognome modificato (Lascia vuoto per non cambiare) ")
    dataN = input("Inserisci la data di nascita modificata (Lascia vuoto per non cambiare) ")
    if cognome:
        dati_da_modifcare[1] = cognome
    if dataN:
        dati_da_modifcare[2] = dataN
    if nome:
        dati_da_modifcare[3] = nome
    return dati_da_modifcare

def DeleteCittadino():
    return input("Inserisci il codice fiscale della persona da eliminare ")

def Login():
    username = input("Inserisci l'username ")
    password = input("Inserisci la password ")
    return {username: [password]}

while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login")
        print("2. Registrazione")
        print("3. Esci")
        login = input("Cosa vuoi fare? ")
        if login == '1':
            api_url = base_url + '/login'
            accesso = Login()
            try:
                response = requests.post(api_url,json=accesso, verify=False)
                print(response.content)
                if str(response.content) == "b'True'":
                    auth = True
                print(auth)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '2':
            api_url = base_url + '/registrazione'
            jsonDataRequest = Login()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '3':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Inserisci cittadino (es. atto di nascita)")
            print("2. Richiedi cittadino (es. cert. residenza)")
            print("3. Modifica cittadino (es. cambio residenza)")
            print("4. Elimina cittadino (es. trasferim altro comune)")
            print("5. Logout")
            print("6. Esci")
            sOper = input("Cosa vuoi fare? ")
            if sOper == "1":
                print("Richiesto atto di nascita")
                api_url = base_url + "/add_cittadino"
                jsonDataRequest = GetDatiCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "2":
                print("Richiesto cittadino")
                api_url = base_url + "/read_cittadino"
                jsonDataRequest = GetCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "3":
                print("Richiesto cittadino")
                api_url = base_url + "/update_cittadino"
                jsonDataRequest = UpdateCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "4":
                print("Richiesto cittadino")
                api_url = base_url + "/delete_cittadino"
                jsonDataRequest = DeleteCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "5":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="6":
                print("Buona giornata!")
                sys.exit()  
