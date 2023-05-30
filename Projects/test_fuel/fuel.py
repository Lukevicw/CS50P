def main():
    result = input("Enter a fraction: ")
    result = convert(result)
    result = gauge(result)
    print(result)


def gauge(percentage):
    n = int(percentage)
    if n >= 99:
        return "F"
    elif n <=1:
        return "E"
    else:
        return (f"{n}%")
        #return percentage + "%"

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            fraction_x = int(x)
            fraction_y = int(y)
            number = (fraction_x/fraction_y) * 100
            if x > y:
                fraction = input("Enter a fraction: ")
            return int(number)
        except (ValueError, ZeroDivisionError):
            raise

    """ except TypeError:
            raise TypeError
        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError
        except AssertionError:
            return AssertionError """

        #convert(input("Enter a fraction: "))
        #main()
        #return
        #continue








if __name__ == "__main__":
    main()




