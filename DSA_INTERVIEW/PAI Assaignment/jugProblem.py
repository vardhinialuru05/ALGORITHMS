def measure(jug1Capacity,jug2Capacity,target):
    if jug1Capacity + jug2Capacity < target:
        return False
    def gcd(x,y):
        while y != 0:
            x,y = y,x%y
        return x
    flag = gcd(jug1Capacity,jug2Capacity)
    if target % flag == 0:
        return True
    else:
        return False
print(measure(2,6,5))
