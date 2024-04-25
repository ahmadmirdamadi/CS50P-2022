q = input("whats your num? ")
q = q.strip()

if q == "42":
    print("yes")
elif q == "forty-two" or q == "forty two" or q == "FoRty TwO":
    print("yes")
else:
    print("no")
