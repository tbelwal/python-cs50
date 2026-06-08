# URL types:
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


import re


def main():
    iframe = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    url = get_url(iframe)


# print(url)
def get_url(iframe):
    url_match = re.search(r'src="(.*?)"', iframe)
    # return url_match.group(1)
    print(url_match.group(1), "- From Get URL")
    validate_url(url_match.group(1))


def validate_url(long_url):
    print(long_url, " - From Validate")

    matches = re.search(r"https?://(www\.)?youtube\.com/embed/([\w-]+)", long_url)

    print(matches.group(2), " - Matches From Validate")


main()
