# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters. Return the answer in any order.
# Costraints: 0 <= digits.length <= 4; digits[i] is a digit in the range ['2', '9'].

def phone(digits: str) -> list[str]:
    if '0' in digits or '1' in digits or len(digits)>4:
        raise NotImplementedError('Code is not meant to take more than 4 numbers, excluding 1')
    digits_chart={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    result=[]
    #code
    return result

print(phone('23')) #["ad","ae","af","bd","be","bf","cd","ce","cf"]