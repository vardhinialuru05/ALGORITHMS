def replace(string, oldChar, newChar):
    result = ""
    for char in string:

        if char == oldChar:
            result += newChar
        else:
            result += char
    return result

string = "aabbcc"
print(replace(string, "a", "x"))

#timecomplexity: O(n)
#spacecomplexity:O(n^2)---> bcoz in result first it is storing a then aa then aab......
#so n(n+1/2) --O(n^2)

    
