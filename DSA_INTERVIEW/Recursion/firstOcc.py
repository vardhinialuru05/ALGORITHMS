def occ(list,key, i= 0):
    if i == len(arr) :
        return -1
    else:
        if list[i] == key:
            return i
        else:
            return occ(list,key,i + 1)

arr = [1,2,3,4]
key = 2
print(occ(arr,key))
