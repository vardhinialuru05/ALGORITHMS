def sumOff(n):
    if n == 0:
        return 0
    else:
        return n + sumOff(n-1)

n = int(input("enter the number"))
print(sumOff(n))