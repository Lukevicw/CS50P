#Define Main Function
def main():
    sentence = input()
    convert(sentence)

#Define Conversion Function
def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    print(x)

main()