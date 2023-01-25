def printNos(n):
    if n == 1:
        print(1, end =" ")
    else:
        printNos(n-1)
        print(n, end =" ")

n = int(input("enter the number"))
printNos(n)