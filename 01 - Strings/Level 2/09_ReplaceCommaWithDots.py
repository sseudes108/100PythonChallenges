string = input("What is the phrase with , ?\n")

for _ in string:
    if _ == ",":
        _ = "."
    print(_,end="")