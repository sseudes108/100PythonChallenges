word = input("Qual a palavra?\n")
index = int(input("Qual o indice a ser removido?\n"))
indexAt = 0

if(len(word) > 0):
    for i in word:
        if indexAt != index:
            print(word[indexAt], end="")
        indexAt += 1
else:
    print("")