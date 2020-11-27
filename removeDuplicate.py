def removeDuplicate(data):
    newList = []
    seen = set()

    for item in data:
        if item not in seen:
            seen.add(item)
            newList.append(item)
    return newList

data = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

print(removeDuplicate(data))