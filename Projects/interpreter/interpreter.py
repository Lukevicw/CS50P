expression = input("Input formula: ")
x, y, z = expression.split(" ")
mathx = float(x)
mathz = float(z)
if y == "+":
    solution = mathx + mathz
elif y == "-":
    solution = mathx - mathz
elif y == "/":
    solution = mathx / mathz
elif y == "*":
    solution = mathx * mathz

print(solution)