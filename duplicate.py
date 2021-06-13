#!usr/bin/python3
def findDuplicate(list,name):
    pos = []
    count = 0
    for i in list:
        if(i==name):
            count += 1
            continue
        
    return count

list = ['pawan','anil','pawan']
item = input("Enter the search item in the list:")

#if __name__ == "__main__()":
count = findDuplicate(list,item)
if(count == 0):
    print("No Duplicate found in list for item:",item)
else:
    print("{} Duplicates found for item {} ".format(count,item))
