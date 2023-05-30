import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[1-9])\s([A|P][mM])\sto\s(1[0-2]|[1-9])\s([A|P][mM])$", s)
    rematches = re.search(r"^(1[0-2]|[1-9]):([0-5]?[0-9])\s([A|P][mM])\sto\s(1[0-2]|[1-9]):([0-5]?[0-9])\s([A|P][mM])$", s)
    if (matches) or (rematches):

        try:
    #If a simple short time is found
            if matches:
                #AM to AM
                if (matches.group(2) == "AM") & (matches.group(4) == "AM"):
                    fix1 = matches.group(1)
                    fix2 = matches.group(3)
                    fix1 = int(fix1)
                    fix2 = int(fix2)
                    if (fix1 < 10):
                        fix1 = "0" + f"{fix1}"
                    if fix2 < 10:
                        fix2 = "0" + f"{fix2}"
                    if fix1 == 12:
                        fix1 = 0
                        fix1 = str(fix1)
                        fix1 = "0" + f"{fix1}"
                    if fix2 == 12:
                        fix2 = 0
                        fix2 = str(fix2)
                        fix2 = "0" + f"{fix2}"
                    fix1 = str(fix1)
                    fix2 = str(fix2)
                    return fix1 + ":00 to " + fix2 + ":00"

                #AM to PM
                elif (matches.group(2) == "AM") & (matches.group(4) == "PM"):
                    fix1 = matches.group(1)
                    fix2 = matches.group(3)
                    fix1 = int(fix1)
                    fix2 = int(fix2)
                    if fix1 == 12:
                        fix1 = "00"
                    elif fix1 < 10:
                        fix1 = "0" + f"{fix1}"
                    else:
                        fix1 = str(fix1)

                    if fix2 == 12:
                        fix2 = str(fix2)
                    else:
                        fix2 = fix2 + 12
                        fix2 = str(fix2)
                    fix1 = str(fix1)
                    fix2 = str(fix2)
                    return fix1 + ":00 to " + fix2 + ":00"

                #PM to PM
                elif (matches.group(2) == "PM") & (matches.group(4) == "PM"):
                    fix1 = matches.group(1)
                    fix1 = int(fix1)
                    if fix1 == 12:
                        fix1 = 0
                    else:
                        fix1 = fix1 + 12
                    fix1 = str(fix1)

                    fix2 = matches.group(3)
                    fix2 = int(fix2)
                    if fix2 == 12:
                        fix2 = 0
                    else:
                        fix2 = fix2 + 12
                    fix2 = str(fix2)
                    return fix1 + ":00 to " + fix2 + ":00"

                #PM to AM
                elif (matches.group(2) == "PM") & (matches.group(4) == "AM"):
                    fix1 = matches.group(1)
                    fix2 = matches.group(3)
                    fix1 = int(fix1)
                    fix2 = int(fix2)
                    if (fix2 < 10):
                        fix2 = "0" + f"{fix2}"
                    if fix2 == 12:
                        fix2 = 0
                        fix2 = str(fix2)
                        fix2 = "0" + f"{fix2}"
                    if fix1 == 12:
                        fix1 = 0
                        fix1 = str(fix1)
                        fix1 = "0" + f"{fix1}"
                    else:
                        fix1 = fix1 + 12
                    fix1 = str(fix1)
                    fix2 = str(fix2)
                    return fix1 + ":00 to " + fix2 + ":00"



    #If a :00 long time is found
            elif rematches:
                #AM to AM
                if (rematches.group(3) == "AM") & (rematches.group(6) == "AM"):
                    fix1 = rematches.group(1)
                    fix2 = rematches.group(4)
                    fix1 = int(fix1)
                    fix2 = int(fix2)
                    if (fix1 < 10):
                        fix1 = "0" + f"{fix1}"
                    if fix2 < 10:
                        fix2 = "0" + f"{fix2}"
                    if fix1 == 12:
                        fix1 = 0
                        fix1 = str(fix1)
                        fix1 = "0" + f"{fix1}"
                    if fix2 == 12:
                        fix2 = 0
                        fix2 = str(fix2)
                        fix2 = "0" + f"{fix2}"
                    fix1 = str(fix1)
                    fix2 = str(fix2)

                    return fix1 + ":" + rematches.group(2) + " to " + fix2 + ":" + rematches.group(5)
                #AM to PM
                elif (rematches.group(3) == "AM") & (rematches.group(6) == "PM"):
                    fix1 = rematches.group(1)
                    fix2 = rematches.group(4)
                    fix1 = int(fix1)
                    fix2 = int(fix2)
                    if (fix1 < 10):
                        fix1 = "0" + f"{fix1}"
                    if fix1 == 12:
                        fix1 = 0
                        fix1 = str(fix1)
                        fix1 = "0" + f"{fix1}"
                    if fix2 == 12:
                        fix2 = str(fix2)
                    else:
                        fix2 = fix2 + 12
                    fix1 = str(fix1)
                    fix2 = str(fix2)
                    return fix1 + ":" + rematches.group(2) + " to " + fix2 + ":" + rematches.group(5)
                #PM to PM
                elif (rematches.group(3) == "PM") & (rematches.group(6) == "PM"):
                    fix1 = rematches.group(1)
                    fix1 = int(fix1)
                    if fix1 == 12:
                        fix1 = str(fix1)
                    else:
                        fix1 = fix1 + 12
                    fix1 = str(fix1)

                    fix2 = rematches.group(4)
                    fix2 = int(fix2)
                    if fix2 == 12:
                        fix2 = str(fix2)
                    else:
                        fix2 = fix2 + 12
                        fix2 = str(fix2)
                    return fix1 + ":" + rematches.group(2) + " to " + fix2 + ":" + rematches.group(5)
                #PM to AM
                elif (rematches.group(3) == "PM") & (rematches.group(6) == "AM"):
                    fix1 = rematches.group(4)
                    fix1 = int(fix1)
                    if fix1 == 12:
                        fix1 = str(fix1)
                    else:
                        fix1 = fix1 + 12
                        fix1 = str(fix1)

                    fix2 = rematches.group(4)
                    fix2 = int(fix2)
                    if fix2 == 12:
                        fix2 = "00"
                    elif fix2 < 10:
                        fix2 = str(fix2)
                        fix2 = ("0" + f"{fix2}")
                    else:
                        fix2 = str(fix2)
                    return fix1 + ":" + rematches.group(2) + " to " + fix2 + ":" + rematches.group(5)

        except:
            raise ValueError

    else:
        raise ValueError






if __name__ == "__main__":
    main()







    #Old Simple Short Regex ^(1[0-2]|[1-9])\s([A|P][mM])\sto\s(1[0-2]|[1-9])\s([A|P][mM])$
    #New Long Included Regex "^(1[0-2]|[1-9])([: ])*(([0-5])([0-9]))*\s([A|P][mM])\sto\s(1[0-2]|[1-9])([: ])*(([0-5])([0-9]))*\s([A|P][mM])"
