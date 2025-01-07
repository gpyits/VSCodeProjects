import requests
import json

SERVER_URL = 'http://127.0.0.1:8080'

def cerca_casa_vendita():
    response = requests.post(f"{SERVER_URL}/CercaCasaVendita", json={})
    if response.status_code == 200:
        return response.json()
    return []

def cerca_casa_affitto():
    response = requests.post(f"{SERVER_URL}/CercaCasaAffitto", json={})
    if response.status_code == 200:
        return response.json()
    return []

def registra_vendita(codice_catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita):
    response = requests.post(f"{SERVER_URL}/RegistraVendita", json={'codice_catastale': codice_catastale, 'data_vendita': data_vendita,'filiale_proponente': filiale_proponente, 'filiale_venditrice': filiale_venditrice, 'prezzo_vendita': prezzo_vendita})
    return response

def registra_affitto(codice_catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto):
    response = requests.post(f"{SERVER_URL}/RegistraAffitto", json={'codice_catastale': codice_catastale, 'data_affitto': data_affitto, 'filiale_proponente': filiale_proponente, 'filiale_venditrice': filliale_venditrice, 'prezzo_affitto': prezzo_affitto, 'durata_contratto': durata_contratto})
    return response

def ottieni_statistiche_mensili(data_inizio, data_fine):
    pass

def calcola_guadagno(data_inizio, data_fine):
    pass

while(True):
    print("Operazioni disponibili:")
    print("0. Registrazione/Login")
    print("1. Cerca casa in vendita")
    print("2. Cerca casa in affitto")
    print("3. Registra vendita")
    print("4. Registra affitto")
    print("5. Ottieni statistiche mensili")
    print("6. Calcola guadagno")
    print("7. Esci")
    operazione = input("Cosa vuoi fare? ")

    if operazione == "1":
        print("\nRicerca delle case in vendita\n")
        case = cerca_casa_vendita()
        if case:
            numero=1
            for casa in case:
                print(f"Casa {numero}")
                print(f"Catastale: {casa['catastale']}")
                print(f"Indirizzo: {casa['indirizzo']} {casa['numero_civico']}")
                print(f"Piano: {casa['piano']}")
                print(f"Metri: {casa['metri']} m²")
                print(f"Vani: {casa['vani']}")
                print(f"Prezzo: {casa['prezzo']}€")
                print(f"Stato: {casa['stato']}")
                print(f"Filiale Proponente: {casa['filiale_proponente']}")
                print('\n\n')
                numero+=1
        else:
            print('\nNessuna casa in vendita al momento\n')

    elif operazione == "2":
        print("\nRicerca delle case in vendita\n")
        case = cerca_casa_affitto()
        if case:
            numero=1
            for casa in case:
                print(f"Casa in affitto {numero}")
                print(f"Catastale: {casa['catastale']}")
                print(f"Indirizzo: {casa['indirizzo']} {casa['numero_civico']}")
                print(f"Numero civico: {casa['numero_civico']}")
                print(f"Tipo affitto: {casa['tipo_affitto']}")
                print(f"Bagno personale: {casa['bagno_personale']}")
                print(f"Prezzo mensile: {casa['prezzo_mensile']}€")
                print(f"Filiale Proponente: {casa['filiale_proponente']}")
                print('\n\n')
                numero+=1
        else:
            print('\nNessuna casa in affitto al momento\n')
    
    elif operazione == "3":
        #vendite_casa(catastale,data_vendita,filiale_proponente,filiale_venditrice, prezzo_vendita)
        codice_catastale = input("Inserisci il codice catastale della casa da registrare come venduta: ")
        data_vendita = input("Inserisci la data della vendita della casa da registrare come venduta: ")
        filiale_te = input("Inserisci la filiale proponente della casa da registrare come venduta: ")
        filiale_venditrice = input("Inserisci la filiale venditrice della casa da registrare come venduta: ")
        prezzo_vendita = input("Inserisci il prezzo di vendita della casa da registrare come venduta: ")

        response = registra_vendita(codice_catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita)
        if response.status_code == 200:
            print("\nVendita registrata con successo.")
        else:
            error_message = response.json().get('message', 'Errore nella registrazione della vendita.')
            print(f"Errore: {error_message}")

    elif operazione == "4":
        #affitti_casa(catastale,data_affitto,filiale_proponente,filiale_venditrice, prezzo_affitto, durata_contratto)
        codice_catastale = input("Inserisci il codice catastale della casa da registrare come affittata: ")
        data_affitto = input("Inserisci la data di affitto della casa da registrare come affittata: ")
        filiale_proponente = input("Inserisci la filiale proponente della casa da registrare come affittata: ")
        filiale_venditrice = input("Inserisci la filiale venditrice della casa da registrare come affittata: ")
        prezzo_affitto = input("Inserisci il prezzo dell'affitto della casa da registrare come affittata: ")
        durata_contratto = input("Inserisci la durata del contratto della casa da registrare come affittata: ")

        response = registra_affitto(codice_catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto)
        if response.status_code == 200:
            print("\nAffitto registrato con successo.")
        else:
            error_message = response.json().get('message', 'Errore nella registrazione dell\'affitto.')
            print(f"Errore: {error_message}")

    elif operazione == "7":
        print("\nUscendo...")
        break