def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def len_check(plate):  # Plate Length check
    return 2 <= len(plate) <= 6


def two_letter_check(
    plate,
):  # Check - “All vanity plates must start with at least two letters.”
    return plate[:2].isalpha()


def number_check(
    plate,
):  # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    for i, char in enumerate(plate):
        if char.isdigit():
            if char == "0":
                return False
            return plate[i:].isdigit()
    return True


def no_puncs(plate):  # No periods, spaces, or punctuation marks are allowed.
    return plate.isalnum()


def is_valid(s):
    return len_check(s) and two_letter_check(s) and number_check(s) and no_puncs(s)


if __name__ == "__main__":
    main()
