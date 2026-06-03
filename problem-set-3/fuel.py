# 1. Get Fraction as per rules. x>=0 int, y>0 int
# 2. Get percentage and E or F


def main():
    level = get_fraction("Fraction: ")
    if level <= 1:
        print("E")
    elif level < 99:
        print(f"{level}%")
    else:
        print("F")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if 0 <= x <= y and y > 0:
                return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
