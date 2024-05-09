# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
# Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction.

def atm_machine(account_name: str):
    account=[account_name, float(input(f'Creating account {account_name}, please write starting balance: '))]
    if account[1]<0:
        print('Error, please input a positive account balance'), atm_machine(account_name)
    action=input('Please select action [deposit/withdraw/check/exit] ').lower()
    while action!='exit':
        action=input(f'Check balance selected\nCurrent balance: {account[1]}\nPlease select action [deposit/withdraw/check/exit] ').lower() if action=='check' else action
        deposit_withdraw=float(input(f'{action[0].upper()+action[1:]} money selected\nSelect quantity to {action} >')) if action in ['deposit', 'withdraw'] else 0
        if deposit_withdraw>=0: 
            account[1]+=deposit_withdraw if action=='deposit' else -deposit_withdraw
            if account[1]<0: 
                account[1]+=deposit_withdraw
                action=input(f'Error: insufficient balance.\nPlease select action [deposit/withdraw/check/exit] ').lower()
            else: 
                action=input(f'Action {action} successful\nPlease select action [deposit/withdraw/check/exit] ').lower() if action!='exit' else 'exit'
        else: 
            action=input(f'Error: invalid input "{deposit_withdraw}". Cannot {action} negative amount of money.\nPlease select action [deposit/withdraw/check/exit] ').lower() if action!='exit' else 'exit'
        action=input(f'Error: invalid input "{action}"\nPlease select action [deposit/withdraw/check/exit] ').lower() if action not in ['deposit', 'withdraw', 'check', 'exit'] else action
    print('Thank you for using our service')
    return account
        
atm_machine('account1')