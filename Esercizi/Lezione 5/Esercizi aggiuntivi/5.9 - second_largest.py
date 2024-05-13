#Implement a function to find the second largest element in an unsorted list without using sorting algorithms.

#without sorting
def second_largest(input_list: list) -> int:
    #removes smallest number unntil there are two left
    for i in range(len(input_list)-2):
        input_list.remove(min(input_list))
    #returns the smallest remaining, hence the second largest
    return min(input_list)

#with sorting
def second_largest(input_list: list) -> int:
    return sorted(input_list)[-2]

print(second_largest([1, 200, 300, 42]))

