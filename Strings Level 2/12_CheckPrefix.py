word = input("What is the word?\n")
prefix = input("What is the prefix?\n")

prefixLenght = len(prefix)

word = word[:prefixLenght]

if word == prefix:
    print(True)
else:
    print(False)