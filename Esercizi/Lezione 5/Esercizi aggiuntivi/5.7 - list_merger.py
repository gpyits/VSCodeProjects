# Implement a function to merge two sorted lists into a single sorted list.

def list_merger(list_1: list, list_2: list) -> list:
    return sorted(list_1+list_2)

print(list_merger([1, 2, 3, 4], [5, 6, 7, 8]))