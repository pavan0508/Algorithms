#!usr/bin/python3
import time
def bubble_sort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(0,length-1):
            if (list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        return list
list = [1,4,2,7,8,3]
s = time.time()
for i in range(len(list)-1):
    n = bubble_sort(list)
print(n)
print("Time taken ms:",s)