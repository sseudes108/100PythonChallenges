listA = []
listB = [1,2]
updatedList = []

for i in listA:
    if listB.__contains__(i):
        pass
    else:
        updatedList.append(i)
print(updatedList)