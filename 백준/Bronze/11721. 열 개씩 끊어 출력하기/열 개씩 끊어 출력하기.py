word = input()
def slicing(syntax):
    while len(syntax) >= 10:
        print(syntax[0:10])
        syntax = syntax[10:]

    else:
        print(syntax)
        return

slicing(word)