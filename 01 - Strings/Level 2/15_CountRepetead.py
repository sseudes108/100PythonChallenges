word = input("What is the word?\n")
charsList = []

repeatCount = 0
charsRepeteadList = []

for char in word:
    if charsList.__contains__(char) is False:
        charsList.append(char)
    else:
        if charsRepeteadList.__contains__(char) is False:
            repeatCount += 1
            charsRepeteadList.append(char)

print(repeatCount)
if(len(charsRepeteadList) > 0):
    for _ in sorted(charsRepeteadList):
        print(_,end=" ")
else:
    print(None)