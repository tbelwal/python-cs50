# 1. Get item input
# 2. If recurring item maintain count
# 3. On Ctrl+d print count + item in item alpha order in all caps


def main():
    grocery_list = get_list()  # Call list function

    for item in sorted(grocery_list):
        print(grocery_list[item], item)


def get_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            return grocery_list
        else:
            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1


if __name__ == "__main__":
    main()
