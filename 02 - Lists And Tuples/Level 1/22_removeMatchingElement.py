list = ["a","b","c","b"]
elementToRemove = 7
hasToRemove = list.count(elementToRemove)

if len(list) == 0:
    print("Empty List")
else:
    if (hasToRemove > 0):
        while hasToRemove > 0:
            list.remove(elementToRemove)
            hasToRemove -= 1
        print(list)
    else:
        print("Not Found")
