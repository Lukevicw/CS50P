import sys
from tabulate import tabulate
import csv

pizzas = []

def main():

    try:
        commandcheck()
        #pizzaFile = open(sys.argv[1])
        #rows = rows.readlines(pizzaFile)
        with open(sys.argv[1], "r") as file:
            #reader = csv.DictReader(file)
            reader = csv.reader(file)
            for line in reader:
                    #pizzas.append({"Regular Pizza": line["Regular Pizza"], "Small": line["Small"], "Large": line["Large"]})
                    pizzas.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(pizzas[1::], headers=pizzas[0], tablefmt="grid"))
    #print(tabulate(pizzas))



def commandcheck():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")




if __name__ == "__main__":
    main()