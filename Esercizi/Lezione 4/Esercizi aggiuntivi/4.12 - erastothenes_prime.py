# Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
# Initialize an array of all numbers up to the limit, marking each number as prime initially.
# Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
# The remaining unmarked numbers are the prime numbers within the limit.
# Return the list of prime numbers.

def is_prime(number: int) -> bool:
    j=2
    while j<number//2:
        if number%j==0:
            return False
        else:
            j**=2
    return True

def eratosthenes_sieve(limit: int):
    pass


print(eratosthenes_sieve)