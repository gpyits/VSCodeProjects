# Develop a function to check if a given number is an Armstrong number (the sum of its digits raised to the power of the number of digits equals the number itself).

def armstrong(num: int) -> bool:
    numbers=[num]
    while num>0:
        numbers.append(num%10)
        num//=10
    return sum([i**(len(numbers)-1) for i in numbers[1:]])==numbers[0]

print(armstrong(153))