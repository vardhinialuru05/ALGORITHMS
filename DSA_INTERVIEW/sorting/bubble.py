def bubble(list):
    index = 0
    while index < len(list) - 1:
        if list[index] < list[index + 1]:
            index += 1
        else:
            list[index],list[index+1] = list[index+1],list[index]
            index += 1
    return list

list= [1,5,2,4,7,8,9]
print(bubble(list))