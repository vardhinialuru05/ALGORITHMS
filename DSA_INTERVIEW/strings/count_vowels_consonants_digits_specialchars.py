# def counter(string):
#     v = c = d = s = 0
#     for char in string.lower():
#         if char == "a" or char == "e" or char =="i" or char == "o" or char == "u" :
#             v += 1
#         elif char >= "a" and char <= "z":
#             c += 1
#         elif char >= "0" and char <= "9":
#             d += 1
#         else :
#             s += 1
#     return v,c,d,s

# string = "aabb123@#$"
# print(counter(string))

# def freequency(list):
#     array = []
#     count = 1
#     maxCount = 1
#     list.sort()
#     for i in range(1,len(list)):
#         if list[i-1] == list[i]:
#             count += 1
#         else:
#             count -= 1
#         maxCount = max(count,maxCount)
#         if maxCount <= count:
#             maxElement = list[i-1]
#     return maxCount, maxElement

# print(freequency([1,6,7,1,3,4,3,1,1,2]))
