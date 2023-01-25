def binary(list,start,end,value):

    if start <= end:
        mid = start + (end-start)//2

        if list[mid] == value:
            return mid
        elif list[mid] < value:
            return binary(list,mid + 1,end,value)
        else:
            return binary(list,start,mid - 1,value)
            
    else:
        return -1

list = [2,3,6,1,5]
start = 0
end = len(list) - 1
print(binary(list,start,end,3))