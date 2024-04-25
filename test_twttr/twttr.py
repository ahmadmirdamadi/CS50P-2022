def main():

    peygham = input("enter: ")
    peyghamz = shorten(peygham)
    print("khoroji:"+peyghamz)

def shorten(word):
    wordz = ""
    for item in word:
        if not item.lower() in ['a' , 'e' , 'i' , 'o' , 'u']:
            wordz += item
    return wordz

if __name__ == "__main__":
    main()