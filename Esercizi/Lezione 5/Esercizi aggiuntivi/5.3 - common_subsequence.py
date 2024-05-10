# Given two strings, find the length of the longest common subsequence (LCS) between them. 
# An LCS is a subsequence of one string that is also a subsequence of the other string while maintaining the relative order of elements.

def common_subsequence(string1: str, string2: str) -> str:
    #subsequences list
    subsequences=[]
    #subsequence can't be longer than the shortest word
    max_subsring_length=max([len(string1), len(string2)])
    #creates two iterables, appends r to j length from sequence if it's an LCS
    for r in range(max_subsring_length):
        for j in range(max_subsring_length):
            if string1[r:j]==string2[r:j] and string1[r:j]!='':
                subsequences.append(string1[r:j])
    #returns subsequence with the highest length
    return max(subsequences, key=len) if subsequences!=[] else None

print(common_subsequence('ciaocomestai', 'ciao'))