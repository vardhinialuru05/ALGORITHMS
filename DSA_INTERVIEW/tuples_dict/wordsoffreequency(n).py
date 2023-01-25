def findFrequency(string, k):
    list = string.split()
    dict = {}
    for char in list:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in dict:
        if dict[char] == k:
            print(char)
findFrequency("this is god god", 1)   