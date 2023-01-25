import math,sys

def minsq(n):

    if n == 0:
        return 0
        
    root = int(math.sqrt(n))
    ans = sys.maxsize
    for i in range(1,root+1):
        curr = 1 + minsq(n-(i*i))
        ans = min(ans,curr)
    return ans

x = minsq(41)
print(x)
