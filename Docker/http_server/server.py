from flask import Flask, render_template, request

utenti=[['Topolino', 'topolino@gmail.com', 'CodiceFiscale', '0']]

api=Flask('__name__')

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/submit', methods=['GET', 'POST'])
def get_code():
    fname=request.form['fname']
    mail=request.form['mail']
    cf=request.form['cf']
    for utente in utenti:
        if utente[0]==fname and utente[1]==mail and utente[2]==cf:

api.run(host='0.0.0.0', port=8088)