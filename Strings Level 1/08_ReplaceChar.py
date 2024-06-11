word = input("Qual a palavra?\n")

cur_char = "W"
new_char = "A"

for _ in word:
    if _ == cur_char:
        _ = new_char
    print(_, end="")