import re
import sys


def main():
    print(parse(input("HTML: ")))



def parse(s):
    s = s.replace("></iframe>", "")
    splitter = s
    splitter = splitter.split(" ")
    isolator = None
    for i in splitter:
        if i := re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]+)", i):
            url = i
            isolator = url.groups()
            return ("https://youtu.be/"+isolator[3])
    if isolator == None:
        return None


if __name__ == "__main__":
    main()