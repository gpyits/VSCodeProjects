# Given a list of integers, find the length of the longest increasing subsequence within the list. 
# An increasing subsequence is a sequence of elements from the array where each element is greater than or equal to the previous element.

def longest_subsequence(sequence: list[int]) -> int:
    #subsequences list
    subsequences=[]
    #creates two iterables, appends r to j length from sequence if it's an increasing subsequence
    for r in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[r:j]==sorted(sequence[r:j]):
                subsequences.append(len(sequence[r:j]))
    #returns maximum subsequence length
    return max(subsequences)

print(longest_subsequence([1, 2, 3, 7, 5, 6, 1]))