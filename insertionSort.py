def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    
    return data

data = [9, 5, 1, 4, 3]
print(insertionSort(data))