# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

def merge_k(k_list: list[list[int]]) -> list:
    result=[]
    for list in k_list:
        result.extend(list)
    return sorted(result)

print(merge_k([[1,4,5],[1,3,4],[2,6]]))