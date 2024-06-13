# lists = [[1,2,3],[4,5,6],[7,8,9]]
# lists = [1,2,3,4,5,6,[7,8,9]]
lists = [["a","b","c"],["d","e","f"],["g","h","i"]]

flattedList = []

for listItem in lists:
    if isinstance(listItem, list):
        for item in listItem:
            flattedList.append(item)
    else:
        flattedList.append(listItem)

print(flattedList)