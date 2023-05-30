import re

name = input("What's your name?: ")

matches1 = re.search(r"^(.+), *(.+)$", name) # The parentheses represents groups which the search function will return
if matches1:
    last, first = matches1.groups()
    name = f"{first} {last}"
print(f"hello {name}")

matches2 = re.search(r"^(.+), (.+)$", name)


if matches2:
    last = matches2.group(1)
    first = matches2.group(2)



url = input("URL: ").lstrip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
        print(f"Username: ", matches.group(1))