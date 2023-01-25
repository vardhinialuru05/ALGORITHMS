def mergeSortedLists(list1, list2):
    i = j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    while i < len(list1):
        result.append(list1[i])
        i +=1

    while j < len(list2):
        result.append(list2[j])  
        j +=1  

    return result    

b = [0, 2, 4] 
a = [100, 101, 102]
print(mergeSortedLists(a, b))           