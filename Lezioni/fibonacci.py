def fibonacci(number):
    if number<=2:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

def fibonacci_iter(number):
    if number in (0, 1):
        return 1
    #this skips two steps 
    num1, num2=0, 1
    #number-1 to go two steps under
    for r in range(number-1):
        num1, num2=num2, num1+num2
        #and therefore number-2 to call two steps before
        if r==number-2:
            return num2

print(fibonacci(6), fibonacci_iter(6))