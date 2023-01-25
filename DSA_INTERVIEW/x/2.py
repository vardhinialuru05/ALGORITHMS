def result(list1, list2):
    list3 = []
    for ele in list1:
        if ele % 2 == 0:
            list3.append(ele)
    for ele in list2:
        if ele % 2 != 0:
            list3.append(ele) 
    return list3  

list1 = [5,10,15,20,25,30,35]
list2 = [7,16,21,26,35,44]

print(result(list1, list2))