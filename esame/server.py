from flask import Flask, request, jsonify
import json
from datetime import datetime

api = Flask(__name__)

def load_database():
    with open('database.json', 'r') as db_file:
        return json.load(db_file)

def save_database(data):
    with open('database.json', 'w') as db_file:
        json.dump(data, db_file, indent=4)

@api.route('/CercaCasaVendita', methods=['POST'])
def cerca_casa_vendita():
    db = load_database()
    criteri = request.json
    case_vendita = db['case_in_vendita']
    risultati = [casa for casa in case_vendita if all(
        criteri.get(chiave, casa[chiave]) == casa[chiave] for chiave in criteri)]
    return jsonify(risultati)

@api.route('/CercaCasaAffitto', methods=['POST'])
def cerca_casa_affitto():
    db = load_database()
    criteri = request.json
    case_affitto = db['case_in_affitto']
    risultati = [casa for casa in case_affitto if all(
        criteri.get(chiave, casa[chiave]) == casa[chiave] for chiave in criteri)]
    return jsonify(risultati)

@api.route('/RegistraVendita', methods=['POST'])
def registra_vendita():
    codice_catastale = request.json.get("codice_catastale")
    data_vendita = request.json.get("data_vendita")
    filiale_proponente = request.json.get("filiale_proponente")
    filiale_venditrice = request.json.get("filiale_venditrice")
    prezzo_vendita = request.json.get("prezzo_vendita")
    with open('database.json', 'r') as db_file:
        db = json.load(db_file)
    casa_vendita = next((casa for casa in db['case_in_vendita'] if casa['catastale'] == codice_catastale), None)
    if casa_vendita:
        casa_vendita = {'codice_catastale': codice_catastale, 'data_vendita': data_vendita, 'filiale_proponente': filiale_proponente, 'filiale_venditrice': filiale_venditrice, 'prezzo_vendita': prezzo_vendita}
        db['vendite_casa'].append(casa_vendita)
        db['case_in_vendita'].remove(casa_vendita)
        with open('database.json', 'w') as db_file:
            json.dump(db, db_file, indent=4)
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'message': 'Casa non trovata nella lista delle case in vendita.'}), 404

@api.route('/RegistraAffitto', methods=['POST'])
def registra_affitto():
    codice_catastale = request.json.get("codice_catastale")
    with open('database.json', 'r') as db_file:
        db = json.load(db_file)
    casa_affitto = next((casa for casa in db['case_in_affitto'] if casa['catastale'] == codice_catastale), None)
    if casa_affitto:
        casa_affito = {'codice_catastale': codice_catastale, 'data_affitto': data_affitto, 'filiale_proponente': filiale_proponente, 'filiale_venditrice': filiale_venditrice, 'prezzo_affitto': prezzo_affitto, 'durata_contratto': durata_contratto}
        db['affitti_casa'].append(casa_affitto)
        db['case_in_affitto'].remove(casa_affitto)
        with open('database.json', 'w') as db_file:
            json.dump(db, db_file, indent=4)
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'message': 'Casa non trovata nella lista delle case in affitto.'}), 404

@api.route('/StatisticheMensili', methods=['POST'])
def statistiche_mensili():
    pass

@api.route('/GuadagnoFiliale', methods=['POST'])
def guadagno_filiale():
    pass

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080, debug=True)
