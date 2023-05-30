import sys
from pyfiglet import Figlet
import random
figlet = Figlet()


fonts = figlet.getFonts()


if len(sys.argv) == 1:
    text = input ("Input: ")
    set_font = figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))
elif ((sys.argv[1] == "-f") or (sys.argv[1] == "--font")) and (sys.argv[2] in fonts):
    text = input("Input: ")
    set_font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
else:
    sys.exit("OMG I'M LEARNING LOL!!!")