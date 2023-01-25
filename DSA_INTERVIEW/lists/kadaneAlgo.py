#we find only positive subarray sum

def kadaneAlgo(list):
    maxSum = -10**9
    tempSum = 0

    for ele in list:
        tempSum += ele

        if tempSum > maxSum:
            maxSum = tempSum
        
        if tempSum < 0:
            tempSum = 0

    return maxSum        

print(kadaneAlgo([1,2,3,-4,5]))

