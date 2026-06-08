import sys
import csv
from tabulate import tabulate


def main():

    print(process_file(sys.argv))


def process_file(comm_args):
    # Evaluate command line argument
    if len(comm_args) < 2:
        sys.exit("Too few command-line arguments")
    if len(comm_args) > 2:
        sys.exit("Too many command-line arguments")
    if not comm_args[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(comm_args[1]) as file:
            return tabulate_csv(file)
    except FileNotFoundError:
        sys.exit("File does not exist")


def tabulate_csv(file):
    menu_rows = list(csv.reader(file))
    return tabulate(menu_rows, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()
