import sys
from pyfiglet import Figlet
import random


def main():
    fig_fonts = Figlet().getFonts()

    match len(sys.argv):
        case 1:  # 0 args
            get_figlet(random.choice(fig_fonts))
        case 3:  # 2 Args
            if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fig_fonts:
                sys.exit("Invalid usage")
            get_figlet(sys.argv[2])
        case _:
            sys.exit("Invalid usage")


def get_figlet(f):
    text = input("Input: ")

    print("Output: ")
    print(Figlet(font=f).renderText(text))


if __name__ == "__main__":
    main()
