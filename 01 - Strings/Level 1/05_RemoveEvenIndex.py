word = input("What is the word?\n")

lenght = len(word)

if(lenght > 1):
    for i in range(lenght):
        if i % 2 != 0:
            print(word[i], end="")
else:
    print(word)