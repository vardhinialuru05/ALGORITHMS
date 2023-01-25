def result(arr, i = 0):
    if i == len(arr):
        return 0
    else:
        return arr[i] + result(arr, i+1)

arr = [1,2,3,1]
print(result(arr))