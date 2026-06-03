def main():
    time = input("Enter time: ")
    float_time = convert(time)

    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    colon_index = time.find(":")
    hours = float(time[:colon_index])
    mins = float(time[colon_index + 1 :])

    return hours + mins / 60


if __name__ == "__main__":
    main()
