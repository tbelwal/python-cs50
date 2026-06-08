import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
        for add_value in matches.groups():
            # Reject leading zeros
            if len(add_value) > 1 and add_value.startswith("0"):
                return False
            # Reject out of 0-255 range values
            if int(add_value) not in range(256):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
