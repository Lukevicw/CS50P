while True:
    fraction = input("Enter a fraction: ")
    try:
        x, y = fraction.split("/")
        fraction_x = int(x)
        fraction_y = int(y)
        number = fraction_x/fraction_y
        number = number * 100
        number = round(number)
        if number <= 100:
            break
    except (ValueError, ZeroDivisionError):
        pass

n = number

if n >= 99:
        print("F")
elif n <=1:
        print("E")
else:
    print(f"{n}%")