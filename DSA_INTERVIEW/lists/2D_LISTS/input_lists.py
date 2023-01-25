# # 2 4
# # 1 2 3 4
# # 4 5 6 7

# row, col = input().split()
# row = int(row)
# col = int(col)

# matrix = []

# while row > 0:
#     list = [int(ele) for ele in input().split()]
#     matrix.append(list)
#     row -= 1
# print(matrix)

# 2 3
# 1 2 3 4 5 6

row, col = input().split()
row = int(row)
col = int(col)
list = [int(x) for x in input("enter elements").split()]
matrix = []

for i in range(row):
    temp = []
    for j in range(col):
        temp.append(list[i*col + j])
    
    matrix.append(temp)
print(matrix)






