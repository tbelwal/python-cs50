def main():
    user_input = input("Enter string: ")
    print(convert(user_input))


def convert(input_string):
    updated_string = input_string.replace(":)", "🙂").replace(":(", "🙁")
    return updated_string


main()
