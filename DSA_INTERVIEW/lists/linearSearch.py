n = int(input("no of digits"))
str = input("enter the values")
list = str.split()
newList = []
counter = 0
flag = False

for x in list:
    newList.append(int(x))
    counter+=1
    if counter == n:
        print(newList)
        break 

key = int(input("enter the key"))

for element in newList:
    if key == element:
        flag = True
        break
print(flag)