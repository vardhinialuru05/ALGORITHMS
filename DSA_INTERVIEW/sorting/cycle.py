def cycle(list):
    index = 0
    while index < len(list):
        correct = list[index] - 1
        if index != correct:
            list[index],list[correct] = list[correct],list[index]
        else:
            index += 1
    return list

list = [1,3,2,4]
print(cycle(list))