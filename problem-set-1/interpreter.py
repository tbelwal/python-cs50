def main():
    # Get expression
    expression = input("Enter Expression: ").strip()

    components = extract(expression)

    match components[1]:
        case "+":
            sum = float(components[0]) + float(components[2])
            print(f"{sum:.1f}")
        case "-":
            diff = abs(float(components[0]) - float(components[2]))
            print(f"{diff:.1f}")
        case "*":
            mult = abs(float(components[0]) * float(components[2]))
            print(f"{mult:.1f}")
        case "/":
            div = float(components[0]) / float(components[2])
            print(f"{div:.1f}")


def extract(expression):
    return expression.split()


if __name__ == "__main__":
    main()
