#!usr/bin/python3
def linear_search(list,n):
    for i in range(len(list)):
        if(list[i] == n):
            return i
    return "notfound"
list = [1,23,23,12,5]
n = int(input("enter the search element"))
pos= linear_search(list,n)
if(pos != "notfound"):
    print("found",pos)
else:
    print(pos)
