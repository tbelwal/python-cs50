import sys
import csv


def main():

    process_file(sys.argv)


def process_file(comm_args):
    # Evaluate command line argument
    if len(comm_args) < 3:
        sys.exit("Too few command-line arguments")
    if len(comm_args) > 3:
        sys.exit("Too many command-line arguments")
    if not comm_args[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(comm_args[1]) as file:
            create_output(file, comm_args[2])
    except FileNotFoundError:
        sys.exit("File does not exist")


def create_output(file, output):

    reader = csv.DictReader(file)
    with open(output, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]

            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()
