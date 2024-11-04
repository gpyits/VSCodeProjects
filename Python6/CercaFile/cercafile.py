import requests, json, sys
import subprocess
from myjson import *
import urllib3
from cercastringa import *
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = 'AIzaSyB_jCxqJnXIhE_sPAlkvb4keVz_80D9Abc'


def ComponiJsonPerImmagine(sImagePath, sImgName):
  subprocess.run(["rm", f"./{sImgName}.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath, f"./{sImgName}.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:

        if iOper == 1:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Errore di comunicazione con il server")


print("Cerca un file in base a una parola chiave") 
api_url = base_url + sGoogleApiKey

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Cerca un file")
    print("2. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero")
        continue

    if iOper == 1:

        sParolaChiave = input('Immetti la parola chiave: ') 
        sRoot = input("Inserisci la directory di ricerca: ")
        sOutDir = input("Inserisci la directory di output: ")

        for root, dirs, files in os.walk(sRoot):
            sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
            print(sToPrint)

            for sFile in files:
                if sFile[-4:]=='.jpg':
                    sDomanda = 'Riassumi in poche parole il contenuto di questa foto'+f'\ntraduci nella lingua di questa parola: {sParolaChiave}'
                    ComponiJsonPerImmagine(sFile, sImgName=os.path.basename(sFile))
                    dJsonRequest = JsonDeserialize("request.json")
                    dJsonRequest["contents"][0]["parts"][0]["text"] = sDomanda
                    response = requests.post(api_url, json=dJsonRequest, verify = False)

                    if sParolaChiave in response:
                        os.system(f'cp {sFile} {sOutDir}/{sFile}')

                elif sFile[-4:]=='.pdf':
                    if CercaInFilePdf(sFile=sFile, sString=sParolaChiave):
                        os.system(f'cp {sFile} {sOutDir}/{sFile}')

                elif sFile[-4:]=='.docx' or sFile[-4:]=='.doc':
                    if CercaInFileDoc(sFile=sFile, sString=sParolaChiave):
                        os.system(f'cp {sFile} {sOutDir}/{sFile}')

                else:
                    if CercaStringaInFileName(sFilename=sFile, sStringToSearch=sParolaChiave):
                        os.system(f'cp {sFile} {sOutDir}/{sFile}')

    elif iOper == 2:
        print("Uscendo...")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprovare")