# def repeatedNumber(A):
#     A = list(A)    
#     A.sort()
#     i = 1
    
#     while i < len(A):
#         if A[i-1] == A[i]:
#             repeat = A[i]
#             break
#         else:
#             i += 1
    
#     while i <= len(A):
#         if i not in A:
#             miss = i
#             break
#         else:
#             i += 1

#     return repeat, miss

# A = (1,2,2,3,5)
# print(repeatedNumber(A))


def sum(arr):
    flag = 0
    for ele in arr:
        flag += ele
    return flag

def sumS(arr):
    flag = 0
    for ele in arr:
        flag += ele*ele
    return flag

def result(arr):
    n = len(arr)
    s = n*(n+1)/2
    sS = n*(n+1)*(2*n+1)/6
    x = s - sum(arr)
    y = sS - sumS(arr)

    z = y/x 

    miss = (x + z )//2
    repeat = (z - x )//2
    return miss, repeat

arr = (1,2,2,3,5)
print(result(arr))



    