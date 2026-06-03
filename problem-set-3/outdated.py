# Get date as MM/DD/YYYY or Month Date, YYYY. Reject all else
# Month should be <=12 or from List
# date should be max 31


def main():
    print(get_date())


def get_date():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    while True:
        user_date = input("Date: ")
        try:
            if len(user_date.split("/")) == 3:
                m = int(user_date.split("/")[0])
                d = int(user_date.split("/")[1])
                y = int(user_date.split("/")[2])
                if 1 <= m <= 12 and 1 <= d <= 31 and y > 0:
                    return f"{y:04}-{m:02}-{d:02}"
            elif len(user_date.split(",")) == 2:
                y = int(user_date.split(",")[1].strip())
                m = months[user_date.split(",")[0].split()[0]]
                d = int(user_date.split(",")[0].split()[1])
                if 1 <= m <= 12 and 1 <= d <= 31 and y > 0:
                    return f"{y:04}-{m:02}-{d:02}"
            else:
                continue
        except (ValueError, IndexError, KeyError):
            continue


main()
