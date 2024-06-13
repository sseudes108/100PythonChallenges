from itertools import permutations

list = [1,2,3]

perm = permutations(list)

for item in perm:
    newList = []
    for i in item:
        newList.append(i)
    print(newList)