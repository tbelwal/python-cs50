def main():
    greeting = input("Enter Greeting: ").lower().strip()

    print(greeting_fine(greeting))


def greeting_fine(greeting):
    # print(greeting[:4])
    if greeting[:5] == "hello":
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


main()
