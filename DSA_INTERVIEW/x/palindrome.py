def palindrome(string): 
    l = 0
    r = len(string) - 1
    while l <= r:
        if string[l] == string[r]:
            l += 1
            r -= 1
            continue
        else:
            return False
    return True    

print(palindrome("oiio"))