word = input("Qual a palavra?\n")
hasNumber = False

for _ in word:
    if _.isdigit() == True:
        hasNumber = True
        break

if hasNumber == True:
    print(True)
else:
    print(False)