
# PARTE 1
# Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
# La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
#  
# PARTE 2
# Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. 
# Questa funzione dovrebbe aggiornare il dizionario del contatto.


def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contact = {'profile': name, 'email': email, 'telefono': telefono}
    return contact

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if name!=None:
        dictionary['profile'] = name
    if email!=None:
        dictionary['email'] = email
    if telefono!=None:
        dictionary['telefono'] = telefono
    return dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))