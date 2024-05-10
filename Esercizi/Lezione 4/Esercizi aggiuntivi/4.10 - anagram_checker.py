# Create a function that checks whether two given strings are anagrams of each other.
# Convert both strings to lowercase and remove any non-alphabetic characters.
# Sort the characters of each string and compare the sorted strings for equality.
# Indicate whether the strings are anagrams or not.

#does everything, pretty straighforward
def anagram_checker(word1: str, word2: str) -> bool:
    return sorted(''.join(i for i in word1 if 97<=ord(i)<=122).lower())==sorted(''.join(i for i in word2 if 97<=ord(i)<=122).lower())

print(anagram_checker('abcb', 'cbab'))