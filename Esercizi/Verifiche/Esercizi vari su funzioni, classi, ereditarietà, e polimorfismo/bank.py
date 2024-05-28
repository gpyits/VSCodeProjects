# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.id=account_id
        self.balance=balance
    def deposit(self, amount: float) -> None:
        self.balance+=amount
    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str, Account]=[]
    def create_account(self, account_id: str) -> None:
        self.accounts.append(Account(account_id, 0))
    def deposit(self, account_id: str, amount: float) -> None:
        account=[account for account in self.accounts if account.id==account_id]
        if account==[]: return 'Utente non trovato'
        account[0].deposit(amount)
    def get_balance(self, account_id: str) -> float:
        return [account for account in self.accounts if account.id==account_id][0].get_balance()
    

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123")) #100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456")) #200