import random
def loop():
    try:
        while True:
            n = int(input("Level: "))
            if n < 0:
                continue
            elif type(n) is str:
                continue
            else:
                global x
                x = n
                break
    except TypeError:
        loop()
    except ValueError:
        loop()
loop()

maximum = x
number = random.randint(0, x)

def gametime():

    try:

        while True:
            y = int(input("Guess: "))

            if y < 0:
                continue
            elif type(y) is str:
                continue
            elif y == number:
                print("Just right!")
                break
            elif y < number:
                print("Too small!")
                continue
            elif y > maximum:
                print("Too large!")
                continue
            elif y > number:
                print("Too large!")
                continue

    except TypeError:
        gametime()
    except ValueError:
        gametime()

gametime()
