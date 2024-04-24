import time
a=[i for i in range(1, (10**4)+1)]

def bubble_sort(list):
    start=time.time()
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                dummy=list[j]
                list[j]=list[j+1]
                list[j+1]=dummy
    return list, time.time()-start

def bubble_sort_improved(list):
    start=time.time()
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                dummy=list[j]
                list[j]=list[j+1]
                list[j+1]=dummy
    return list, time.time()-start

#see pdf on moodle
def flag_bubble_sort(list):
    pass

print(bubble_sort(a[::-1]))
print(bubble_sort_improved(a[::-1]))