word = "Wonderful"

#print the first three letters
def Firsts(word):
    for i in range(3):
        print(word[i], end="")

#print the last three letters
def Lasts(word):
    length = len(word) - 3
    # i starts at 0
    for i in range(3):
        print(word[length + i], end="")
        
if len(word) > 6:
    Firsts(word)
    Lasts(word)
else:
    print("")