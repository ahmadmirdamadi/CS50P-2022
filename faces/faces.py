def main():
    x = str(input("enter your text: "))
    print(convert(x))


def convert(y):
    y = y.replace(":)","🙂")
    y = y.replace(":(" , "🙁")
    return y

main()