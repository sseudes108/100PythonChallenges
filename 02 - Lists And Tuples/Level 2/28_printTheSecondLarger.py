list = [2]

if len(list) > 1:
    sorted = sorted(list, reverse = True)
    if(len(sorted) > 0):
        print(sorted[1])
    else:
        print(None)
else:
    print(None)