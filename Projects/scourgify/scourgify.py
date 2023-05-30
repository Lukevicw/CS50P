import csv
import sys

def main():
    characters = []
    commandcheck()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                #print(row)
                seperate = row["name"].split(",")
                #print(seperate)
                characters.append({"first": seperate[1].lstrip(), "last": seperate[0], "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[2], "w") as file:
        write = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        write.writerow({"first": "first", "last": "last", "house": "house"})
        for row in characters:
            write.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

    #print(characters)

def commandcheck():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()