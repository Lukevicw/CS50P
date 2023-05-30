def main():
    value = input("What time is it?: ")
    time = convert(value)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >= 18 and time <=19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    fminutes = float(minutes) / 60
    return float(hours) + fminutes


if __name__ == "__main__":
    main()