# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

# An input string is valid if: 
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
def is_valid_parenthesis(s: str) -> bool:
    if s=='':
        return True
    elif s=='()' or s=='[]' or s=='{}':
        return True
    elif len(s)==2 and (s!='()' or s!='[]' or s!='{}'):
        return False
    else:
        s=[i for i in s]
        for r in range(len(s)-1):
            if s[r]+s[r+1]=='()' or s[r]+s[r+1]=='[]' or s[r]+s[r+1]=='{}':
                s.pop(r), s.pop(r)
                return is_valid_parenthesis(''.join(s))
    return False
            
print(is_valid_parenthesis("(]"))