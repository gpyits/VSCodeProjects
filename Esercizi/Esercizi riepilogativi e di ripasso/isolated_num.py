# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(nums: list[int]) -> int:
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return 1
    elif len(nums)==2:
        return 0 if nums[0]==nums[1] else 2
    else:
        count=0
        for r in range(1, len(nums)-1):
            if nums[r]!=nums[r-1] and nums[r]!=nums[r+1]:
                count+=1
        count+=1 if nums[0]!=nums[1] else 0
        count+=1 if nums[-1]!=nums[-2] else 0
        return count

print(count_isolated([1, 2, 3, 4, 5])) #expected 5
print(count_isolated([1, 2]))