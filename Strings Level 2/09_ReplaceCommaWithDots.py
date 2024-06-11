string = input("Qual a frase com , ?\n")

for _ in string:
    if _ == ",":
        _ = "."
    print(_,end="")