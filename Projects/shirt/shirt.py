import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    commandcheck()

    try:
        img = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = ImageOps.fit(img, size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def commandcheck():
    check1 = False
    check2 = False
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
        check1 = True
    if sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        check2 = True

    if (check1 == False):
        sys.exit("Input is false")
    if (check2 == False):
        sys.exit("Output is false")

    img1 = splitext(sys.argv[1])
    img2 = splitext(sys.argv[2])

    if img1[1].lower() != img2[1].lower():
        sys.exit("Input and output have different extensions")



if __name__ == "__main__":
    main()