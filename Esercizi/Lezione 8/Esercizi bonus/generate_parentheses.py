# Generate Parentheses: 
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
import itertools

def check_parentheses(expression: str) -> bool:
    if expression=='()':
        return True
    elif expression==')(' or expression=='(' or expression==')':
        return False
    else:
        expression=[i for i in expression]
        for r in range(len(expression)-1):
            if expression[r]+expression[r+1]=='()':
                expression.pop(r), expression.pop(r)
                return check_parentheses(''.join(expression))

def generate_par(n: int) -> list[str]:
    return list(set([''.join(j for j in i) for i in list(itertools.permutations(['(' for i in range(n)]+[')' for i in range(n)], n*2)) if check_parentheses(''.join(j for j in i))]))

print(generate_par(3))
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

print(generate_par(1))
# Example 2:
# Input: n = 1
# Output: ["()"]