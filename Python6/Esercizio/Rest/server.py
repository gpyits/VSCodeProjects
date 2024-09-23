from flask import Flask, json, request

cittadini = [{"nome": "Mario", "cognome": "Rossi", "dataNascita": "20/02/1990","codFiscale":"dfcged90b28h501u"},
             {"nome": "Mario", "cognome": "Bianchi", "dataNascita": "20/02/1990","codFiscale":"dfcged90b28h501u"},
             {"nome": "Giuseppe", "cognome": "Verdi", "dataNascita": "20/12/1956","codFiscale":"dfcvds90b28h501u"}]

api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def process_json():
    print("Ricevuta chiamata")
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        print(jsonReq)
        cittadini.append(jsonReq)
        jsonResp = {"Esito":"200", "Msg":"ok"}
        return json.dumps(jsonResp)
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)