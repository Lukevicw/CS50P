lst = []

try:

    while True:
        names = lst.append(input("Name: "))

except EOFError:
    if len(lst) == 1:
        lst = str(lst)
        blst = lst.strip("[]")
        blst = blst.replace("'", "")
        print("Adieu, adieu, to " + blst)
    elif len(lst) == 2:
        lastName = lst[-1]
        last = lastName.strip("[]")
        last = lastName.replace("'", "")
        del lst[-1]
        lst = str(lst)
        blst = lst.strip("[]")
        blst = blst.replace("'", "")
        print("Adieu, adieu, to " + blst + " and " + last)
    else:
        lastName = lst[-1]
        last = lastName.strip("[]")
        last = lastName.replace("'", "")
        del lst[-1]
        lst = str(lst)
        blst = lst.strip("[]")
        blst = blst.replace("'", "")
        print("Adieu, adieu, to " + blst + ", and " + last)

