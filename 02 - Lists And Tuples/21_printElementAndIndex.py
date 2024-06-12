list = [1,2,3,4,5]
index = 0

if len(list) < 1:
    print("Empty List")
else:
    for item in list:
        print(item,end=" ")
        print(index)
        index += 1