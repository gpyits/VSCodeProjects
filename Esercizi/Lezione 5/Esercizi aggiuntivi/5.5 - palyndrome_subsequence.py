# A palindrome is a word, phrase, or sequence that reads the same backwards as forward. 
# Given a string, the task is to find the longest palindrome subsequence within the string. 
# A subsequence is obtained from a string by deleting zero or more elements without changing the order of the remaining elements.

def palindrome_subsequence(input_string: str) -> str:
    #base case
    if input_string==input_string[::-1]:
        return input_string 
    #adds every possible palindrome substring
    palindrome_subsequences=[]
    for i in range(len(input_string)):
        for j in range(len(input_string)):
            if input_string[i:j]==input_string[i:j][::-1]:
                palindrome_subsequences.append(input_string[i:j])
    #returns the longest one
    return max(palindrome_subsequences, key=len)

print(palindrome_subsequence('abdgirafariglòasdfdadkaq'))