listA = [4,5,6]
listB = [1,2,3]
commomElements = []

for item in listA:
    if listB.__contains__(item):
        commomElements.append(item)
print(commomElements)