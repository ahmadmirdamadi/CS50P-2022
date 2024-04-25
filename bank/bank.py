a = input("enter: ")

if a.startswith("Hello"):
    print("$0")

elif a.startswith(" Hello "):
    print("$0")

elif a.startswith("H"):
    print("$20")

else:
    print("$100")