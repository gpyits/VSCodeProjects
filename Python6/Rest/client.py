import requests, json

base_api_url = "http://127.0.0.1:8080/"

def StampaMenuOperazioni():
    print("1. Inserisci cittadino")
    print("2. Leggi dati cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    comando = input("Inserisci operazione: ")
    return comando
    
def print_dictionary(dData):
    for keys, values in dData.items():
        print(keys + " - " + values)
        
def GetDatiCittadino():
    nome = input("Inserisci nome: ")
    cognome = input("Inserisci cognome: ")
    dataN = input("Inserisci data nascita(dd/mm/yyyy): ")
    codF = input("Inserisci codice fiscale: ")
    datiCittadino = {"nome":nome, "cognome": cognome, "dataNascita":dataN, "codFiscale":codF}
    return datiCittadino

print("Cosa vuoi fare?") 
comando = StampaMenuOperazioni()
print("Comando inserito: " + comando)
if comando=="1":
    api_url = base_api_url + "add_cittadino"
    jsonDataRequest = GetDatiCittadino()
    response = requests.post(api_url,json=jsonDataRequest)
    #print(response.json())
    print(response.status_code)
    print(response.headers["Content-Type"])
    data1 = response.json()
    if (type(response.json()) is dict):
        print_dictionary(response.json())

if comando == "2":
    api_url = base_api_url + "read_cittadino"
    jsonDataRequest = GetDatiCittadino()
    response = requests.post(api_url,json=jsonDataRequest)

if comando == "3":
    api_url = base_api_url + "modifica_cittadino"

if comando == "4":
    pass

if comando == "5":
    pass