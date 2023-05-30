def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#First two are letters
    if s[0:1].isalpha() == False:
        return False

#Length of plate
    if len(s) <2 or len(s) >6:
        return False


#No punctuation
    if s.isalnum() == False:
        return False

#First number in plate is not to be a 0
    for letters in s:
        if letters.isdigit():
            num = s.index(letters)
            if s[num:].isdigit() and letters != "0":
                return True
            else:
                return False


    return True


main()