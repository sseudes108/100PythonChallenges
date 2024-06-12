## Sort the string in alphabetical order and lower case

words = input("What are the words?\n")
words = words.lower()
splitedWords = words.split(" ")

for word in splitedWords:
    word = sorted(word)
    for char in word:
        print(char, end="")
    print(" ", end="")