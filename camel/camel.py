cs = input("enter: ")
for c in cs:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c,end="")
print()