def binarySearch(list, key):
    start = 0
    end = len(list)-1

    while start<=end:
        mid = int(start + (end-start)/2)

        if key == list[mid]:
            return True
        elif key > list[mid]:
            start = mid + 1
        else :
            end = mid - 1

    return False

n = int(input("no of digits"))
str = input("enter the values")
li = str.split()
list = []
key=int(input("enter key"))
count = 0

for value in li:
    list.append(int(value))
    count+=1
    
    if count == n:
        break

result = binarySearch(list ,key)
print(result)   
        
    