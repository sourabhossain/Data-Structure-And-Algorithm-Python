def bubbleSort(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                (data[j], data[j + 1]) = (data[j + 1], data[j])
    return data

data = [45, 0, -2, 11, -9]
print(bubbleSort(data))