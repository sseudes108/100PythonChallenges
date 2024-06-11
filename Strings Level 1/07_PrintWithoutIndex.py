word = input("What is the word?\n")
index = int(input("What is the index to be removed?\n"))
indexAt = 0

if(len(word) > 0):
    for i in word:
        if indexAt != index:
            print(word[indexAt], end="")
        indexAt += 1
else:
    print("")