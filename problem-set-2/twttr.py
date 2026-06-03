def main():
    input_string = input("Enter string: ")
    print(twttr_format(input_string))


def twttr_format(input_string):
    vowels = {"a", "e", "i", "o", "u"}
    result = ""
    for char in input_string:
        if char.lower() not in vowels:
            result += char

    return result


if __name__ == "__main__":
    main()
