# get input string
def main():
    input_string = input("Enter Camel Case string: ")
    print(get_snake(input_string))


def get_snake(string):
    result = ""
    for char in string:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


if __name__ == "__main__":
    main()
