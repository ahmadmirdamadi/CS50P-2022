while True:
    fuel = input("enter: ")
    try:
        x,y = fuel.split("/")
        x_j = int(x)
        y_j = int(y)
        a = x_j / y_j

        if a <= 1:
            break

    except(ValueError,ZeroDivisionError):
        print("Error!")

p = (a * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"%{int(p)}")