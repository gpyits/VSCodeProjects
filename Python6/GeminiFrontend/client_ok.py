import requests, json, sys
import subprocess
from myjson import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = 'AIzaSyB_jCxqJnXIhE_sPAlkvb4keVz_80D9Abc'



def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])


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




print("Benvenuti nella mia Generative AI") 
api_url = base_url + sGoogleApiKey

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Crea una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere ad una domanda su un file img")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sArgomento = input("Inserisci l'argomento della favola: " )
        sArgomento2 = "Crea una favola su " + sArgomento + "in italiano"
        jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento2}]}]}
        #jsonDataRequest["contents"][0]["parts"][0]["text"] = sArgomento
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            print(sTestoPrimaRisposta)

    elif iOper == 2:
        sDomanda = input("Inserisci la domanda: ")
        sDomanda += "tradotto in italiano"
        dJsonRequest["contents"][0]["parts"][0]["text"] = sDomanda
        response = requests.post(api_url, json=dJsonRequest, verify = False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            print()
            print(sTestoPrimaRisposta)

    elif iOper == 3:
        sFile = input("Inserisci il path competo del file che vuoi analizzare: ")
        sDomanda = input("Inserisci la domanda: ")
        sDomanda += "tradotto in italiano"
        ComponiJsonPerImmagine(sFile)
        dJsonRequest = JsonDeserialize("request.json")
        dJsonRequest["contents"][0]["parts"][0]["text"] = sDomanda
        response = requests.post(api_url, json=dJsonRequest, verify = False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            print()
            print(sTestoPrimaRisposta)

    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")





