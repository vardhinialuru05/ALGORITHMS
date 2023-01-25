def binary(list,value):
    start = 0
    last = len(list) - 1
    while start <= last:
        mid = start + (last - start)//2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            start = mid + 1
        else:
            last = mid - 1
    return -1

print(binary([1,2,3,4,5,6],5))

