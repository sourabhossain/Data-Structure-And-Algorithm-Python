def mergeSort(data):
    if len(data) > 1:
        index = len(data) // 2
        left = data[:index]
        right = data[index:]

        mergeSort(left)  
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1  
        
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1 
        
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data

data = [21, -1, 7, 8, -5, 54]

print(mergeSort(data)) 