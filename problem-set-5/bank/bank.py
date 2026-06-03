def main():
    greeting = input("Enter Greeting: ").strip()

    print(f"${value(greeting)}")


def value(greeting):
    # print(greeting[:4])
    if greeting[:5].lower() == "hello":
        return 0
    elif greeting[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
