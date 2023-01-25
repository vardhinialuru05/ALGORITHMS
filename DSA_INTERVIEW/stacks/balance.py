from queue import LifoQueue

def balance(expression):
    newStack = LifoQueue(len(expression))

    for char in expression:
        if char == "[" or char == "{" or char ==  "(":
            newStack.put(char)
        elif char == "]" or char == "}" or char == ")":
            if newStack.empty():
                return False
            else:
                top = newStack.get()
                if (char == "]" and top == "[" ) or  (char == "}" and top == "{") or (char == ")" and top == "("):
                    continue
                else:
                    return False
        else:
            continue
    return True

print(balance("[1 + {[} - (2)]"))



