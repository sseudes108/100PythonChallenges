word = input("What is the word?\n")

lenght = len(word)

for _ in word:
    lenght -= 1
    print(word[lenght], end="")