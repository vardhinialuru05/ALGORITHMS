# def identify(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     rowSet = set()
#     colSet = set()
#     for row in range(m):
#         for col in range(n):
#             if matrix[row][col] == 0:
#                 rowSet.add(row)
#                 colSet.add(col)
            
#     for i  in rowSet:
#         for col in range(n):
#             matrix[i][col] = 0
    
#     for j  in colSet:
#         for row in range(m):
#             matrix[row][j] = 0

# matrix = [ [1,2,1], [1,3,1], [2,0,3]]

# identify(matrix)
# print(matrix)

# 
# def setZeroes2(matrix):
#     row = len(matrix)
#     col = len(matrix[0])

#     flag = False

#     for i in range(row):
#         if matrix[i][0] == 0:
#             flag = True

#         for j in range(1, col):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = matrix[0][j] = 0

#     for i in range(row - 1, -1, -1):
#         for j in range(col - 1, 0, -1):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0
#         if flag:
#             matrix[i][0] = 0


# matrix = [ [1,2,1], [1,3,1], [2,0,3]]

# setZeroes2(matrix)
# print(matrix)

# def stock(list):
#     maxSum = -10**9

#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             flag = list[j] - list[i]

#             if flag > maxSum:
#                 maxSum = flag

#     if maxSum < 0:
#         return 0   
#     return maxSum

# list = [7,6,4,3,1]
# print(stock(list)) 

import socket

s = socket.socket()
print ("socket successfully created")

port = 12345

s.bind((socket.gethostname(), port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
print ('got connection from', addr)
c.send('thankyou for connecting')

c.close()


        

        

