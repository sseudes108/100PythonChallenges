import string

matches = 0

text = input("Qual o texto?\n")
text = text.lower()
text = text.replace(" ","")
uniqueLetters = set(text)
uniqueLetters = ''.join(uniqueLetters)

alphabet = string.ascii_lowercase

for i in uniqueLetters:
    for j in alphabet:
        if i == j:
            matches += 1

if(matches == len(alphabet)):
    print(True)
else:
    print("False. Matches: %d. Alphabet: %d" % (matches, len(alphabet)))