from datetime import date
import inflect
import sys

f = inflect.engine()


def main():
    try:
        year, month, day = input("DOB: ").split("-")
    except ValueError:
        sys.exit("Invalid")

    print(life(year, month, day))


def life(year, month, day):
    try:
        birthday = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid"
    today = date.today()
    difference = today - birthday
    minutes = int(difference.total_seconds() / 60)
    final = f.number_to_words(minutes, andword="") + " minutes"
    return final.capitalize()

if __name__ == "__main__":
    main()