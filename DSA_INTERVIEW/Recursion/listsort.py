def result(list,i):
    if i == len(list) - 1:
        return True
    else:
        if list[i] < list[i+1]:
            i += 1
            return result(list, i)
        else:
            return False
    
list = [1,2,3,1]
i = 0
print(result(list,i))