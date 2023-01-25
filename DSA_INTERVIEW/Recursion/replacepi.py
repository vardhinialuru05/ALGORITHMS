
def replace(string,b):
    if len(string)<2:
        return string
    else:
        if string[0:2] == "pi":
            return b + replace(string[2:],b)
        else:
            return string[0] + replace(string[1:],b)


print(replace("piabcpidef","3.14"))
    