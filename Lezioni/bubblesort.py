import time
a=[i for i in range(1, (10**2)+1)]

def bubble_sort(list):
    start=time.time()
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                dummy=list[j]
                list[j]=list[j+1]
                list[j+1]=dummy
    return list, f'{time.time()-start} seconds'

def bubble_sort_improved(list):
    start=time.time()
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                dummy=list[j]
                list[j]=list[j+1]
                list[j+1]=dummy
    return list, f'{time.time()-start} seconds'

def flag_bubble_sort(list):
    start=time.time()
    for i in range(len(list)):
        swap_flag=False
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                swap_flag=True
                dummy=list[j]
                list[j]=list[j+1]
                list[j+1]=dummy
    if swap_flag==False:
        return list, f'{time.time()-start} seconds'

print(bubble_sort(a[::-1]))
print(bubble_sort_improved(a[::-1]))
print(flag_bubble_sort(a[::-1]))