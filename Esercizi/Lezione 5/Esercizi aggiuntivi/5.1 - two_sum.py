#Given a list of integers and a target sum, find all unique pairs of integers within the list that sum up to the target.

def two_sum(numbers_list: list, target_sum: int) -> list[tuple]:
    result=[]
    #creates two iterables, checks if they equal to target sum
    for number1 in numbers_list:
        for number2 in numbers_list:
            #prevents same numbers to be added
            if number1==number2:
                continue
            elif number2+number1==target_sum:
                result.append((number1, number2))
    #removes non-unique pairs
    return result[:(len(result)//2)]

print(two_sum([1, 2, 3, 4, 5, 6, 7], 10))