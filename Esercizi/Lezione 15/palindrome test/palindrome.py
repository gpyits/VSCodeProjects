# Given a string s which consists of lowercase or uppercase letters, 
# write a function that returns the length of the longest palindrome that can be built with those letters. 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
def longest_palindrome(s: str) -> int:
    count=[s.count(l) for l in set(s)]
    lenght=0
    for v in count:
        if v%2==0:
            lenght+=v
            count[count.index(v)]=0
        else:
            lenght+=v-1
            count[count.index(v)]=v-(v-1)
    return lenght if 1 not in count else lenght+1