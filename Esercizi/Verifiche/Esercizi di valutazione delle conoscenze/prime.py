# Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

def prime_factors(n: int) -> list[int]:
    i=2
    result=[]
    while i**2<=n:
        if n%i==0:
            n//=i
            result.append(i)
        else:
            i+=1
    if n>1:
        result.append(n)
    return result

print(prime_factors(99999999999999999999))