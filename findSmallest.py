def findSmallest(data):
    smallest = data[0]
    smallest_index = 0

    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
            smallest_index = i

    return smallest_index


data = [1, 2, 3, 4, 5]

print(findSmallest(data))