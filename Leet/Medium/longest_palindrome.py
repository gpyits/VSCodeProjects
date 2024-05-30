# Given a string s, return the longest palindromic substring in s.

def longest_palindrome_substring(input_string: str) -> str:
    result=[]
    for i in range(len(input_string)):
        for j in range(len(input_string)+1):
            if input_string[i:j]!='' and input_string[i:j]==input_string[i:j][::-1]:
                result.append(input_string[i:j])
    return max(result, key=len)

print(longest_palindrome_substring('babad')) #bab or aba