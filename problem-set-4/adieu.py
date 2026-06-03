# 1. get names one by one till user hits ctrl+d
# 2. get number of names
# 3. print Adieu, p.join

import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    print_adieu(names)


def print_adieu(names):
    print(f"\nAdieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
