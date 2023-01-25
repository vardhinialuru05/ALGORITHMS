def resultant(list):
    start = 0
    end = len(list)-1

    while start < end:

        if list[start] < 0:
            start += 1 
        else:
            if list[end] >= 0:
                end -= 1
            else:
                list[start], list[end] = list[end], list[start]

list = [-2, -4, 0, 7, -5, 2, -6]
resultant(list)
print(list)