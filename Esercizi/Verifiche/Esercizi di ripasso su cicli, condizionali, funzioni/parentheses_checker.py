#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    if expression=='()':
        return True
    elif expression==')(' or expression=='(' or expression==')':
        return False
    else:
        expression=[i for i in expression]
        for r in range(len(expression)-1):
            if expression[r]+expression[r+1]=='()':
                expression.pop(r), expression.pop(r)
                return check_parentheses(''.join(expression))

print(check_parentheses("()()")) #expected True
print(check_parentheses("(()))(")) #expected False
print(check_parentheses("((()))")) #expected True