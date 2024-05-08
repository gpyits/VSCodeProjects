# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
# Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction.

def atm_machine(account_name: str):
    account=[account_name, float(input(f'Creating account {account_name}, please write starting balance: '))]
    #change this
    if account[1]<0:
        raise Exception(print('Error, please input a positive account balance'), atm_machine(account_name))
    action=input('Please select action [deposit/withdraw/check/exit] ').lower()

    while action!='exit':
        if action=='check':
            action=input(f'Check balance selected\nCurrent balance: {account[1]}\nPlease select action [deposit/withdraw/check/exit] ').lower()
        if action=='deposit':
            deposit=float(input('Deposit money selected\nHow much money do you want to deposit? >'))
            #infinite while loop, remove list comprehension
            account[1]+=deposit if deposit>=0 else print('Error: deposited value can\'t be a negative number')
            action=input(f'Successfully added {deposit} money to your account\nPlease select action [deposit/withdraw/check/exit] ').lower()
        if action=='withdraw':
            withdraw=float(input('Withdraw money selected\nHow much money do you want to withdraw? >'))
            #same and separate the two invalid conditions
            account[1]-=withdraw if withdraw<=account[1] and withdraw>=0 else print('Error: insufficient balance') 
            action=input(f'Successfully withdrawn {withdraw} money to your account\nPlease select action [deposit/withdraw/check/exit] ').lower()
    return 'Thank you for using our service'
        
print(atm_machine('account1'))