word = ""
index = 15
indexAt = 0

if(len(word) > 0):
    for i in word:
        if indexAt != index:
            print(word[indexAt], end="")
        indexAt += 1
else:
    print("")