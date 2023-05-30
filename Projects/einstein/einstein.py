#Prompt for Mass
def main():
    mass = int(input("Enter Mass as Integer of Kgs:"))
    convert(mass)

#Calculate for Joules as integer
def convert(n):
    n = n * 90000000000000000
    print(n)

main()