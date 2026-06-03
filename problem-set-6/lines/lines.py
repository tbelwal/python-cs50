import sys


def main():
    # Evaluate command line argument
    print(file_name_check(sys.argv))


def file_name_check(comm_args):
    if len(comm_args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(comm_args) > 2:
        sys.exit("Too many command-line arguments")
    elif not comm_args[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(comm_args[1], "r") as file:
            return count_lines(file)
    except FileNotFoundError:
        sys.exit("File does not exist")


# Count Lines
def count_lines(file):
    code_lines = 0
    for line in file:
        # Check comments
        if line.lstrip().startswith("#"):
            continue
            # Check blanks
        if not line.strip():
            continue

        code_lines += 1

    return code_lines


if __name__ == "__main__":
    main()
