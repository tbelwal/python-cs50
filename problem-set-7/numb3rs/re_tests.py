import re

# input = "123.001.304.888"

# matches = re.findall(r"[0-9]{3}", input)  # findall returns a list
# matches_2 = re.findall(r"\d{3}", input)
# matches_3 = re.search(r"(\d{3})\.(\d{3})\.(\d{3})\.(\d{3})", input)
# matches_4 = re.fullmatch(r"(\d{3})\.(\d{3})\.(\d{3})\.(\d{3})", input)

# print(matches)
# print(matches_2)
# print(matches_3.group())
# print(matches_4.groups())

print(bool(re.fullmatch(r"(\d{3}).(\d{3}).(\d{3}).(\d{3})", "123a456b789c000")))
