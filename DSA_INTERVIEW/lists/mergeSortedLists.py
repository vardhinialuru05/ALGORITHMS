#space complexity is O(1)
def merge(arr1,arr2):

    for i in range(len(arr1)):

        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] =arr2[0], arr1[i]
            
            j = 0
            temp = 0

            while j < len(arr2):

                if arr2[temp] > arr2[j+1]:
                    arr2[temp], arr2[j+1] = arr2[j+1], arr2[temp]
                    temp = j + 1
                    j += 1
                else:
                    break
            i += 1
        else:
            i += 1

    return [arr1,arr2]

print(merge([1, 3, 5, 7], [0, 2, 6, 8, 9]))