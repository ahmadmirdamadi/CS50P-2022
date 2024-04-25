import sys
from os.path import splitext
from PIL import Image,ImageOps

def main():

    check_command_line_argument()

    try:
        aks = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    lebas = Image.open("shirt.png")
    andaze = lebas.size
    ops = ImageOps.fit(aks, andaze)
    ops.paste(lebas, lebas)
    ops.save(sys.argv[2])



def check_command_line_argument():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    pooshe1 = splitext(sys.argv[1])
    pooshe2 = splitext(sys.argv[2])

    if check_extension(pooshe1[1]) == False:
        sys.exit("Invalid input")

    elif check_extension(pooshe2[1]) == False:
        sys.exit("Invalid output")

    elif pooshe1[1].lower() != pooshe2[1].lower():
        sys.exit("Input and output have different extensions")



def check_extension(pooshe):

    if pooshe in [".png" , ".jpg" , ".jpeg"]:
        return True
    return False


if __name__ == "__main__":
    main()