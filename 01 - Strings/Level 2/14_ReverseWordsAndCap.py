words = input("What are the words?\n")

splitedWords = words.split(" ")

def InvertCase(char):
    if char.islower():
        char = char.upper()
    else:
        char = char.lower()
    print(char, end="")

for word in splitedWords:
    lenght = len(word)
    for i in word:
        lenght -= 1
        i = word[lenght]
        InvertCase(i)
    print(" ", end="")