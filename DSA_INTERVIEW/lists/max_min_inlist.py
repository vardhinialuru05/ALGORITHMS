def max_min_Element(list):
    smallest = largest = list[0]

    for number in list:
        if smallest > number:
            smallest = number
        if largest < number:
            largest = number
            
    return smallest, largest

list = [int(x) for x in input("enter values").split()]
print(list)

smallest_element, largest_element = max_min_Element(list)
print(smallest_element, largest_element )

