# Combinations: 
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. 
# You may return the answer in any order.
import itertools

def combinations(n: int, k: int) -> list[list[int]]:
    return [list(i) for i in list(itertools.combinations([i for i in range(1, n+1)], k))]

print(combinations(4, 2))
# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

print(combinations(1, 1))
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
