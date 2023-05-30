def main():
    sentence = input("Say your greeting!: ")
    #sentence = sentence.lower()
    print(value(sentence))


def value(greeting):
    if(greeting.startswith("hello")):
        greeting = 0
        return greeting
    elif(greeting.startswith("h")):
        greeting = 20
        return greeting
    else:
        greeting = 100
        return greeting


if __name__ == "__main__":
    main()