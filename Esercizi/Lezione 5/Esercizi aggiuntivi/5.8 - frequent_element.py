#Create a function that finds the element that appears most frequently in a given list.

def frequent_element(input_list: list):
    #element counter
    result={}
    for element in input_list:
        if element in result:
            result[element]+=1
        else:
            result[element]=1
    #swaps keys with values to return the most frequent one
    return {v:k for k, v in result.items()}[max({v:k for k, v in result.items()})]

print(frequent_element([1, 1, 1, 2, 3, 5, 3, 7, 1]))