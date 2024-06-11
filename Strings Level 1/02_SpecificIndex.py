word = input("Qual a palavra?\n")
index = int(input("Qual o indice desejado?\n"))

if len(word) == 0:
    print("Empty String")
elif index > len(word) - 1:
    print("Index is out of range")
else:
    print(word[index])