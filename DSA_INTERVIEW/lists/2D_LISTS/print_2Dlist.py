def printMatrix(a):
    for list in a:
        for element in list:
            print(element, end = " ")
        print()

a = [[1,2,3],[2,3],[2,4,5]]
printMatrix(a)