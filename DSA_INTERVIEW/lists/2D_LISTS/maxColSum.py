def maxColSum(matrix,row,col):
    index = -1
    maxSum = -10**9

    for i in range(col):
        sum = 0

        for j in range(row):
            sum += matrix[j][i]

            if sum > maxSum :
                maxSum = sum
                idx = i

    return idx

matrix = [[1,2,3],[4,5,6],[7,8,9]]
row = col = 3

print(maxColSum(matrix,row,col))
