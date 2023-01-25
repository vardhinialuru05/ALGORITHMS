def linearSearch(list, key):
    for element in list:
        if element == key:
            return True          
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

result = linearSearch(list ,key)
print(result)