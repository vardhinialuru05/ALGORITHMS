def isVowel(c):
    return ( c == "a" or c == "e" or c == "i" or c == "o" or c == "u"  )
def removeVowels(string):
    for i in range(0,len(string)-1):
        if( isVowel(string[i] ) != True or isVowel(string[i + 1] ) != True):
            print(string[i])
        elif isVowel(string[i]):
            continue
        else:
            print(string[i])

removeVowels("aaqil")