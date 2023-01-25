def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        n1 = fib(n-2)
        n2 = fib(n-1)
        return n1 + n2

n = int(input("enter the number"))
print(fib(n))