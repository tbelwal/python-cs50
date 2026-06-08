import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Check iframe
    if not re.search(r"^<iframe.+</iframe>", s):
        return None

    # Get src url
    if url_match := re.search(r'src="(.*?)"', s):
        return shorten_url(url_match.group(1))
    return None


def shorten_url(u):
    # Check embed and youtube.com and return new url
    if matches := re.search(r"https?://(www\.)?youtube\.com/embed/([\w-]+)", u):
        return "https://youtu.be/" + matches.group(2)
    return None


if __name__ == "__main__":
    main()
