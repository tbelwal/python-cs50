import sys
from PIL import Image, ImageOps
import os


def main():
    # Evaluate command line arguments
    validation_checks(sys.argv)


def validation_checks(comm_args):
    valid_extensions = [".jpg", ".jpeg", ".png"]  # Valid file types

    # Evaluate number of command line arguments
    if len(comm_args) < 3:
        sys.exit("Too few command-line arguments")
    if len(comm_args) > 3:
        sys.exit("Too many command-line arguments")

    # Get file extensions of Input and Output
    in_filetype = os.path.splitext(comm_args[1])[-1]
    out_filetype = os.path.splitext(comm_args[2])[-1]

    # Check file formats using extensions
    if in_filetype.lower() not in valid_extensions:
        sys.exit("Invalid Input Image format")
    if out_filetype.lower() not in valid_extensions:
        sys.exit("Invalid Output image format")
    if in_filetype.lower() != out_filetype.lower():
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(comm_args[1]) as file:
            create_output(file, comm_args[2])  # Send files for processing
    except FileNotFoundError:
        sys.exit("File does not exist")


def create_output(in_file, out_file):
    print("We're in Create Output")
    with Image.open("shirt.png") as shirt:
        resized_input = ImageOps.fit(in_file, shirt.size)
        resized_input.paste(shirt, shirt)
        resized_input.save(out_file)


if __name__ == "__main__":
    main()
