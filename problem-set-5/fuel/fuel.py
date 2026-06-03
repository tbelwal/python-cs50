def main():
    while True:
        try:
            level = convert(input("Fraction: "))
            print(gauge(level))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError
    if x < 0 or y < 0:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"


if __name__ == "__main__":
    main()
