# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def search_insert_positon(array: list[int], target: int) -> int:
    return array.index(target) if target in array else sorted(array+[target]).index(target)

print(search_insert_positon([1,3,5,6], 7))