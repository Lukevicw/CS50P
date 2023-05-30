import validators


def main():
    email = validators.email(input("What's your email?: "))
    if email == True:
        print("Valid")
    else:
        print("Invalid")





if __name__ == "__main__" :
    main()