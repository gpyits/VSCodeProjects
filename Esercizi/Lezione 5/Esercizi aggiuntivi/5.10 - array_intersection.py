#Implement a function to find the elements that are present in both of the two sorted lists.

def array_intersection(list_1: list, list_2: list) -> set:
    return set(list_1).intersection(set(list_2))

print(array_intersection([1, 2, 3, 4], [3, 4, 5, 6]))