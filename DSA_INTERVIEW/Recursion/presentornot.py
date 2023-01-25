def result(arr,ele,i = 0):
    if i == len(arr) :
        return False
    else:
        if arr[i] == ele:
            return True
        else:
            return result(arr,ele,i+1)

arr = [1,2,3,4]
ele = 2
print(result(arr,ele))