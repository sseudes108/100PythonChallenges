word = input("What is the word?\n")
index = int(input("What is the desired index?\n"))

if len(word) == 0:
    print("Empty String")
elif index > len(word) - 1:
    print("Index is out of range")
else:
    print(word[index])