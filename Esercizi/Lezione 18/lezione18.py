# All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. 
# The library must raise custom exceptions to indicate specific errors to the user.
# Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError. 
# Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that 
# (i.e., print the list,  reverse the list, and check whether the list is ordered). 
# Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).

#Exceptions
class SquaredByZeroError(Exception):
    '''Raises error if user tries to square a negative number'''
    pass
class InvalidPasswordError(Exception):
    '''Raises error if user tries to use an invalid password'''
    pass
class AddError(Exception):
    '''Raises error if user tries to add a date already in the database'''
class RemoveError(Exception):
    '''Raises error if user tries to remove a date not in the database'''
    pass
class CreateDateError(Exception):
    '''Raises error if user tries to create date with string not in the format mm.dd.yyyy'''
    pass
class FormulaError(Exception):
    '''Raises error if formula formatting, numbers or operators are invalid'''
    pass
class InvalidFraction(Exception):
    '''Raises error if fraction given is not in the given numerator/denominator format'''
    pass

# Safe Square Root: 
#   Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
#   Handle ValueError if the input is negative by returning an informative message.
import math

def safe_sqrt(number: int) -> int:
    try: return math.sqrt(number)
    except: raise SquaredByZeroError('Must be a positive number')

# Password Validation: 
#   Write a function validate_password(password) that checks if a password meets certain criteria 
#   (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
#   Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
def validate_password(password: str):
    if len(password)>20 and len([i for i in password if i==i.upper()])>=3 and len([i for i in password if i in '!"£$%&&/()[]{}=?^\'-.,;:_><'])>=4:
        return True
    else: raise InvalidPasswordError('Invalid password: must contain more than twenty characters, have at least three uppercase letters and four special characters')

# Context Managers for File Handling: 
#   Use the with statement and context managers to open and close a file. 
#   Handle potential IOError within the with block for clean resource management.
try: 
    with open('Esercizi/Lezione 18/file.txt', 'r') as f:
        lines=f.readlines()
except FileNotFoundError:
    with open('Esercizi/Lezione 18/file.txt', 'a') as f:
        pass

# Database of dates: 
#   Write a class that manages a database of dates with the format gg.mm.aaaa 
#   implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  
#   A query on a given date allows for retrieving a given new date. 
#   Note that a date is an object for your database; it must be instantiated from a string.
class Date:
    def __init__(self, month: int, day: int, year: int) -> None:
        self.month: int=month
        self.day: int=day
        self.year: int=year
    @classmethod
    def create_date(cls, date: str) -> 'Date':
        '''Takes a string containing the date in the format mm.dd.yyyy and converts it into a Date object'''
        if len(date)!=10:
            raise Exception('Cannot create date: wrong date format')
        else:
            month, day, year=map(int, date.split('.'))
            return cls(month, day, year)
    def __str__(self) -> str:
        return f'{self.day}.{self.month}.{self.year}'

class Database:
    def __init__(self, dates_database: list[Date]) -> None:
        self.database: list[Date]=dates_database
    def addDdate(self, date: str) -> None:
        '''Adds a given date in the string format mm.dd.yyyy to the database'''
        date=Date.create_date(date)
        if date not in self.database:
            self.database.append(date)
        else: 
            raise AddError('Error: date is already present in database')
    def removeDate(self, date: str):
        '''Removes a given date in the string format mm.dd.yyyy from the database'''
        date=Date.create_date(date)
        if date in self.database:
            self.database.remove(date)
        else:
            raise RemoveError('Error: date is not present in the database')
    def dateQuery(self, date: str) -> dict[str,int]:
        '''Returns a dictionary containing date data'''
        date=Date.create_date(date); return {'Month':date.month, 'Day':date.day, 'Year':date.year}

# An interactive calculator: 
#   It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! 
#   User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). 
#   Split user input using str.split(), and check whether the resulting list is valid:
#   If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#   Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). 
#   Catch any ValueError that occurs, and instead raise a FormulaError.
#   If the second input is not '+' or '-', again raise a FormulaError.
#   If the input is valid, perform the calculation and print out the result. 
#   The user is then prompted to provide new input, and so on, until the user enters quit.
def calculator(formula: str) -> float:
    '''Takes a mathematic formula by the format "num1 operator num2" and returns the solution'''
    num1, operator, num2=formula.split(' ')
    operator_table={'+':lambda x, y:x+y,
                    '-':lambda x, y:x-y,
                    '*':lambda x, y:x*y,
                    '/':lambda x, y:x/y,
                    '//':lambda x, y:x//y,
                    '**':lambda x, y:x**y,
                    '%':lambda x, y:x%y,}
    #errors
    if len(formula)!=3: #invalid format
        raise FormulaError('Error: input formula is invalid')
    try: 
        num1, num2=float(num1), float(num2)
    except ValueError: #invalid numbers
        raise FormulaError('Error: input formula is invalid')
    try: 
        operator=operator_table[operator]
    except ValueError: #unsupported operator
        raise FormulaError('Error: input formula is invalid')
    #return call if formula passes all errors
    return operator(num1, num2)

# Personalized math library: 
#   Create a Python library that provides functions for handling fractions, with built-in error handling. 
#   The library must include functions for the following operations:
#   Create a fraction from the numerator and denominator.
#   Collect the numerator and denominator of a fraction.
#   Simplify a fraction.
#   Add, subtract, multiply and divide fractions.
#   Check whether one fraction is equivalent to another. 
class fraction: 
    @staticmethod
    def create(numerator: int, denominator: int) -> str:
        try: 
            int(numerator) and int(denominator)
            return f'{numerator}/{denominator}'
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def collect(fraction: str) -> dict[str,int]:
        try:
            if len(fraction.split('/'))!=3: int(None)
            numerator, denominator=map(int, fraction.split('/'))
            return {'Numerator':numerator, 'Denominator':denominator}
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def simplify(fraction: str) -> str:
        try:
            if len(fraction.split('/'))!=3: int(None)
            numerator, denominator, i=map(int, fraction.split('/')), 2
            while True:
                if numerator%denominator==0:
                    numerator//=denominator
                    denominator=1
                    return f'{numerator}/1'
                elif denominator%numerator==0:
                    denominator//=numerator
                    numerator=1
                    return f'1/{denominator}'
                elif numerator%i==0 and denominator%i==0:
                    numerator//=i
                    i=2
                elif i>numerator//2 or i>denominator//2:
                    return f'{numerator}/{denominator}'
                else: 
                    i+=1
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def add(fraction1: str, fraction2: str) -> str:
        try:
            if len(fraction1.split('/'))!=3 or len(fraction2.split('/'))!=3: int(None)
            numerator1, denominator1=map(int, fraction1.split('/'))
            numerator2, denominator2=map(int, fraction1.split('/'))
            return fraction.simplify(f'{(denominator1*denominator2//denominator1*numerator1)+(denominator1*denominator2//denominator2*numerator2)}/{denominator1*denominator2}')
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def subtract(fraction1: str, fraction2: str) -> str:
        try:
            if len(fraction1.split('/'))!=3 or len(fraction2.split('/'))!=3: int(None)
            numerator1, denominator1=map(int, fraction1.split('/'))
            numerator2, denominator2=map(int, fraction1.split('/'))
            return fraction.simplify(f'{(denominator1*denominator2//denominator1*numerator1)-(denominator1*denominator2//denominator2*numerator2)}/{denominator1*denominator2}')
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def multiply(fraction1: str, fraction2: str) -> str:
        try:
            if len(fraction1.split('/'))!=3 or len(fraction2.split('/'))!=3: int(None)
            numerator1, denominator1=map(int, fraction1.split('/'))
            numerator2, denominator2=map(int, fraction1.split('/'))
            return fraction.simplify(f'{numerator1*numerator2}/{denominator1*denominator2}')
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def divide(fraction1: str, fraction2: str) -> str:
        try:
            if len(fraction1.split('/'))!=3 or len(fraction2.split('/'))!=3: int(None)
            numerator1, denominator1=map(int, fraction1.split('/'))
            numerator2, denominator2=map(int, fraction1.split('/'))
            return fraction.simplify(f'{numerator1*denominator2}/{numerator2*denominator1}')
        except ValueError:
            raise InvalidFraction('Invalid fraction input')
    @staticmethod
    def isEquivalent(fraction1: str, fraction2: str) -> bool:
        try:
            if len(fraction1.split('/'))!=3 or len(fraction2.split('/'))!=3: int(None)
            return True if fraction.simplify(fraction1)==fraction.simplify(fraction2) else False
        except ValueError:
            raise InvalidFraction('Invalid fraction input')