def linear(list,value):
    index = 0
    while index < len(list):
        if list[index] == value:
            return index
        else:
            index += 1
    
    return -1

print(linear([1,2,3],4))