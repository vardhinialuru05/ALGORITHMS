def avgValue(string):
    sum = 0
    for i in range(len(string)):
        sum += ord(string[i])
    return sum // len(string)

print(avgValue("HAPPY"))