# Create a function that converts a given integer to its Roman numeral representation.
# Handle numbers from 1 to 3999.
# Use a combination of string manipulation and conditional statements to build the Roman numeral.

#1=I, 5=V, 10=X
#50=L, 100=C
#500=M, 1000=M
#special numbers: 4, 9, 40, 90, 400, 900 

#ones, tens, hundreds, thousands=number%10, (number%100)//10, (number%1000)//100, number//1000
def roman_numeral_conversion(number: int)->str:
    #because of how conversion is handled, I'd need to remove the 4s and 9s and include the directly into the conversion instead as if 4/9 else
    conversion_table={1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'M', 900:'CM', 1000:'M'}
    #checks if number is within allowed range
    if number not in range(1, 4000):
        return False
    #number values as their decimal place value
    pos_values=[number%10, (number%100)//10, (number%1000)//100, number//1000]
    for k, v in conversion_table.items():
        for i in pos_values:
            #check for nearest "5" (make dummy first key for values les than 5) item to the left in the keys,
            #then convert it to the value*(number-5 of the 1 value of that position, e.g. I, X, C, M)
            pass
            

roman_numeral_conversion(3333)