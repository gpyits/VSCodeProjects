# Create a function that converts a given integer to its Roman numeral representation.
# Handle numbers from 1 to 3999.
# Use a combination of string manipulation and conditional statements to build the Roman numeral.

def roman_numeral_conversion(number: int)->str:
    #conveniently arranged conversion table
    conversion_table={1:['I', 'IV', 'V', 'IX'], 2:['X', 'XL', 'L', 'XC'], 3:['C', 'CD', 'D', 'CM'], 4:'M'}
    converted_number=''
    #checks if number is within allowed range
    if number not in range(1, 4000):
        return False
    #number values as their decimal positional value: ones, tens, hundreds, thousands
    pos_values=[number%10, (number%100)//10, (number%1000)//100, number//1000]
    #position flag
    position=1
    for i in pos_values:
        #converts based on the conversion table dictionary
        i=conversion_table[position][0]*i if i<4 else conversion_table[position][1] if i==4 else conversion_table[position][2] if i==5 else conversion_table[position][2]+conversion_table[position][0]*(i-5) if i<9 else conversion_table[position][-1] if i==9 else 'M' if position==4 else None
        converted_number+=i[::-1]
        position+=1
    return converted_number[::-1]

for r in range(1, 4001):
    print(f'{r}: ', roman_numeral_conversion(r))