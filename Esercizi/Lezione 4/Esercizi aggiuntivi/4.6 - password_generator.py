# Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
# Allow the user to specify the password length and desired character types. Generate and return a random password that meets the user's criteria.
import random

#very simplistic method, desired character types turned on by default
def password_generator(password_length: int, want_lowercase=True, want_uppercase=True, want_numbers=True, want_symbols=True):
    desired=['abcdefghijklmnopqrstuvwxyz' if want_lowercase else None, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if want_uppercase else None, 
             '0123456789' if want_numbers else None, ',.-#+^\'\\!"£$%&/()=?[]@_:;<>|' if want_symbols else None]
    desired.remove(None) if None in desired else desired
    password=''.join(desired)
    return ''.join(random.sample(password, password_length))

print(password_generator(30))