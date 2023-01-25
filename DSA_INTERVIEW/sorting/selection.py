def selection(list):
    for i in range(0 ,len(list)):
        minIndex = i
        for j in range(i, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list

list= [1,5,2,4,7,8,9]
print(selection(list))
        


