def quickSort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i <= pivot]
        greater = [i for i in data[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10, 5, 2, 3]))