word = input("What is the word?\n")
hasNumber = False

for _ in word:
    if _.isdigit() == True:
        hasNumber = True
        break

if hasNumber == True:
    print(True)
else:
    print(False)