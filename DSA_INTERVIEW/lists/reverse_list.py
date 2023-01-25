def swap(list, start, end):
    temp = list[start]
    list[start] = list[end]
    list[end] = temp 

# def reverse_list(list):
#     start = 0
#     end = len(list)-1
#     while start < end :
#         swap(list, start, end)
#         start+=1
#         end-=1    



list = [int(x) for x in input("values").split()]
reverse_list(list)
print(list)