def replace(string,a,b):
    if len(string)==0:
        return string
    else:
        if string[0] is a:
            return b + replace(string[1:],a,b)
        else:
            return string[0] + replace(string[1:],a,b)
        

print(replace("aaqil","a","b"))