def occ(list,key, i):
    if i == -1 :
        return -1
    else:
        if list[i] == key:
            return i
        else:
            return occ(list,key,i - 1)

list = [1,2,3,4,2]
i= len(list)-1
key = 2
print(occ(list,key,i))