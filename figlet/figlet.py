import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3:
    isRandomFont = False
else:
    sys.exit(1)



figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


pyam = input('enter: ')
print(f"khoroji {figlet.renderText(pyam)}")