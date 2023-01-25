def sum(a, b, *more):
    sum = a + b

    for ele in more:
        sum += ele
    return sum

print(sum(1,2,3))