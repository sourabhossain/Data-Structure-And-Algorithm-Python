def linearSearch(data, searchItem):
    for i in range(len(data)):
        if data[i] == searchItem:
            return i
    return -1

print(linearSearch([21, 54, 78], 100))