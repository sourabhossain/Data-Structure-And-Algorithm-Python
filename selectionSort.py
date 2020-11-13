def findSmallest(data):
    smallest = data[0]
    smallest_index = 0

    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
            smallest_index = i

    return smallest_index

def selectionSort(data):
    data2 = []

    for i in range(len(data)):
        smallest = findSmallest(data)
        data2.append(data.pop(smallest))
    
    return data2

print(selectionSort([5, 3, 6, 2, 10]))