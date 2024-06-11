word = input("Qual a palavra?\n")

length = len(word)

if(length > 1):
    for i in range(length):
        if i % 2 != 0:
            print(word[i], end="")
else:
    print(word)