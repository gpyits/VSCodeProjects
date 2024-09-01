# Scrivi una funzione che accetti tre parametri: user, passw e stato dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a "67890" e l'account è attivo (True). 
# La funzione ritorna "Ingresso consentito" oppure "Ingresso negato".
def verifica_accesso(user: str, passw: str, stato: bool) -> str:
    return 'Ingresso consentito' if user=='manager' and passw=='67890' and stato else 'Ingresso negato'