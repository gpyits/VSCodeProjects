# Given an integer x, return true if x is a palindrome, and false otherwise.

def palindrome_number(number: int) -> bool:
    return True if str(number)[::-1]==str(number) else False

print(palindrome_number(121))