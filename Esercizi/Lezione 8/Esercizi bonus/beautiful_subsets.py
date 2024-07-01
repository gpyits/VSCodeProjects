# The Number of Beautiful Subsets:
# Write a function with an array nums of positive integers and a positive integer k given as inputs. 
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k. 
# Return the number of non-empty beautiful subsets of the array nums. 
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
# Two subsets are different if and only if the chosen indices to delete are different.
def generate_subsets(array: list) -> list[list]:
    subsets = [[]]
    for elem in array:
        subsets.extend([subset+[elem] for subset in subsets])
    for i in subsets:
        if i==[] or i==array:
            subsets.remove(i)
    return subsets

def is_beautiful(subset: list[int,], k: int) -> bool:
    for i in range(len(subset)-1):
        if abs(subset[i]-subset[i+1])==k:
            return False
    return True

def beautiful_subsets(nums: list[int], k: int) -> int:
    nums=generate_subsets(nums)
    while True:
        for i in range(len(nums)):
            if len(nums[i])>2:
                for j in generate_subsets(nums[i]):
                    nums.append(j)
                nums.remove(nums[i])
        if all(len(i)<=2 for i in nums):
            break
    return len([i for i in nums if is_beautiful(i, k)==True])

print(beautiful_subsets([2, 4, 6], 2))
# Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4

print(beautiful_subsets([2, 4, 6], 2))
# Example 2:
# Input: nums = [1], k = 1
# Output: 1