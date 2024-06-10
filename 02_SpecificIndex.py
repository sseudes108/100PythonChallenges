word = "Hello"
index = 1

if len(word) == 0:
    print("Empty String")
elif index > len(word) - 1:
    print("Index is out of range")
else:
    print(word[index])