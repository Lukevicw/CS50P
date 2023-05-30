import sys

def main():
    checker()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        #print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")
    count_lines = 0
    for line in lines:
        if line.isspace():
            continue
        elif line.lstrip().startswith("#"):
            continue
        else:
            count_lines += 1
    print(count_lines)


def checker():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()