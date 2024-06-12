word = input("What is the word?\n")
sufix = input("What is the sufix?\n")

word = word[len(word) - len(sufix):]
if word == sufix:
    print(True)
else:
    print(False)