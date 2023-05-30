filename = input("Give me your camel and i'll snake it: ")
print("Sssss: ", end="")
for capitals in filename:
    if capitals.isupper():
        print("_" + capitals.lower(), end="")
    else:
        print(capitals, end="")