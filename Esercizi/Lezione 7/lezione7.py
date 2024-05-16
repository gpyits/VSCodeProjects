
# Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.
def divisible_by(num: int, num_range: tuple) -> list:
    return [i for i in range(num_range[0], num_range[1]+1) if i%7==0]

print(divisible_by(7, (2000, 3200)))

# Write a function to calculate the factorial of a number given as input. The number should be returned as output. 
# For example:
#     Input: 8
#     Output: 40320
def factorial(num: int) -> int:
    for i in range(num-1, 1, -1):
        num*=i
    return num

print(factorial(8))

# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. 
# The list is given as input to the function. All factorials should be returned as output. 
# For example:
#     Input: [2, 5, 8, 10]
#     Output: [2, 120, 40320, 3628800]
def factorial_list(numbers: list) -> list:
    return [factorial(number) for number in numbers]

print(factorial_list([2, 5, 8, 10]))

# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs such that i is an integer between 1 and n (both included).
# The function should return the dictionary as output.
# For example:
#     Input: 8
#     Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def dict_gen(num: int) -> dict:
    return {i:i**2 for i in range(1, num+1)}

print(dict_gen(8))

# Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a comma-separated sequence after sorting them alphabetically. 
# For example:
#     Input: without,hello,bag,world
#     Output: bag,hello,without,world
def sort_comma(input_string: str) -> str:
    return ','.join(i for i in sorted([i for i in input_string.split(',')]))

print(sort_comma('without,hello,bag,world'))

# Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising all sentence characters. 
# For example:
#     Input: Practice makes perfect
#     Output: PRACTICE MAKES PERFECT
def capitalize_sentence(input_string: str) -> str:
    return ' '.join(i for i in [i.upper() for i in input_string.split(' ')])

print(capitalize_sentence('Practice makes perfect'))

# Write a function accepting an input string defined with whitespace-separated words and returning it after removing all duplicates and sorting each word alphanumerically. 
# For example:
#     Input: hello world and practice makes perfect and hello world again
#     Output: again and hello makes perfect practice world
def sort_whitespace(input_string: str) -> str:
    return ' '.join(i for i in sorted(list(set([i for i in input_string.split(' ')]))))

print(sort_whitespace('hello world and practice makes perfect and hello world again'))

# Write a function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.
#     Input: The quick brown fox jumps over the lazy dog
#     Output: True
def pangram(input_string: str) -> bool:
    alphabet=[i for i in 'abcdefghijklmnopqrstuvwxyz']
    for letter in input_string:
        if letter in alphabet:
            alphabet.remove(letter)
    return False if alphabet else True

print(pangram('The quick brown fox jumps over the lazy dog'))

# Write a function to check whether a number is "Perfect" or not. 
# In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). 
# For example:
#     Input: 6
#     Output: True
def perfect_number(num: int) -> bool:
    return True if sum([i for i in range(1, num//2+1) if num%i==0])==num else False

print(perfect_number(28))

# Using the code implemented in Exercise 8, write a function that, given a number n as input, computes all "Perfect" numbers between 1 and n. 
# For example:
#     Input: 500
#     Output: [6, 28, 496]
def perfect_numbers(num: int) -> list:
    return [i for i in range(1, num+1) if perfect_number(i)]

print(perfect_numbers(6))

# Write a function to sort the (name, age, height) input list of tuples by ascending order where name is string, age and height are numbers. 
# The function should return a list of tuples of strings. The priority is that name > age > score. 
# Namely, the sort criteria are:
#     Sort based on name;
#     Then, sort based on age;
#     Then, sort by score.

#     Input: [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
#     Output:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]  
def sort_id(input_list: list[tuple]) -> list[tuple]:
    return sorted(input_list)

print(sort_id([('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]))