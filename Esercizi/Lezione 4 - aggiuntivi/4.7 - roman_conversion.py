# Create a function that converts a given integer to its Roman numeral representation.
# Handle numbers from 1 to 3999.
# Use a combination of string manipulation and conditional statements to build the Roman numeral.

def roman_numeral_conversion(number: int)->str:
    #checks if number is within allowed range
    if number not in range(1, 4001):
        return False
    #number values as their decimal place value
    ones, tens, hundreds, thousands=[number%10], [(number%100)//10], [(number%1000)//100], number//1000
    pass
roman_numeral_conversion(3333)