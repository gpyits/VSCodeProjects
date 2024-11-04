import os
import dbclient as db 
import sys
import json

mydb = db.connect()
if mydb is None:
	print("Errore connessione al DB")
	sys.exit()
else:
	print("Connessione avvenuta correttamente")
	

cittadini = {}
with open("anagrafe.json", "r") as json_file:
    cittadini = json.load(json_file)

for key, item in cittadini.items():
	cod_fiscale = key
	nome = item["nome"]
	cognome = item["cognome"]
	data_nascita = item["dataNascita"]
	sQuery = f"insert into cittadini(codice_fiscale,nome,cognome,data_nascita)" 
	sQuery += f" values('{cod_fiscale}','{nome}','{cognome}','{data_nascita}')"
	print(sQuery)
	db.write_in_db(mydb,sQuery)

db.close(mydb)
	