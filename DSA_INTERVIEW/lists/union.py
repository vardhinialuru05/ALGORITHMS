# def doUnion(a,b):
#     new = merge(a,b)
#     count = duplicate(new)
#     return count

# def merge(a,b):
#     result = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     while i < len(a):
#         result.append(a[i])
#         i += 1
#     while j < len(b):
#         result.append(b[j])
#         j += 1   
#     return result    

# def duplicate(list):
#     z = 0
#     while z < len(list) - 1:
#         if list[z] == list[z+1]:
#             list.pop(z+1)
#         else:
#             z += 1
#     return len(list)    

# a = [1, 2, 3]
# b = [4, 1, 5]  
# a.sort()
# b.sort()
# answer = doUnion(a,b)  
# print(answer)
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        a.sort()
        b.sort()
        new = merge(self,
        
        
        
        a,b)
        count = duplicate(new)
        return count
    def merge(a,b):
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while i < len(a):
            result.append(a[i])
            i += 1
        while j < len(b):
            result.append(b[j])
            j += 1   
        return result  
    
    def duplicate(list):
        z = 0
        while z < len(list) - 1:
            if list[z] == list[z+1]:
                list.pop(z+1)
            else:
                z += 1
        return len(list) 