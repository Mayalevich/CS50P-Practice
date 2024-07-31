from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    In = input('Input:')
    print('Output: ' + figlet.renderText(In) )

elif len(sys.argv) ==3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    font = sys.argv[2]
    figlet.setFont(font=font)
    In = input('Input:')
    print('Output: ' + figlet.renderText(In) )

else:
    print('Invalid Input')
    sys.exit(1)
