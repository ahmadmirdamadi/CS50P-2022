aa = input("Enter: ")

x , y , z  = aa.split(" ")

z_jadid = int(z)

x_jadid = int(x)

if y == "+":
    res = x_jadid + z_jadid

if y == "-":
    res = x_jadid - z_jadid

if y == "*":
    res = x_jadid * z_jadid

if y == "/":
    res = x_jadid / z_jadid

print(round(res,1))