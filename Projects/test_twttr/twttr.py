import re

def main():
    tweet = input("Input: ")
    print(shorten(tweet.upper()))



def shorten(word):
    replace = { 'A': '','E': '','I': '', 'O': '','U': '','a': '', 'e': '','i': '','o': '','u': '', '1': '', '2': '','3': '','4': '', '5': '','6': '','7': '','8': '','9': '','0': ''}
    for letters, replacement in replace.items():
        word = re.sub(letters, replacement, word)
    return f"{word}"
    #print(word)


if __name__ == "__main__":
    main()