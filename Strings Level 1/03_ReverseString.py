word = input("Qual a palavra?\n")

length = len(word)

for _ in word:
    length -= 1
    print(word[length], end="")