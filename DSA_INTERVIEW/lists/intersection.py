def intersection(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            p1 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
    return result

print(intersection([1, 2, 3, 4], [2, 3, 5]))

    

