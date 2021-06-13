import time
def binary_search(list,n):
    low = list[0]
    up = list[len(list)-1]
    for i in range(len(list)-1):
        mid = (low+up)/2
        if(n == mid):
            return mid,"found"
        elif(n < mid):
            up = mid-1
        elif(n > mid):
            low = mid+1
        else:
            return "NotFound"
list = [1,2,4,5,24353,31]
s = time.time()
n = int(input("Enter the search element:"))
n,out = binary_search(list,n) 
print(out,n) 
print("Time taken",s)      