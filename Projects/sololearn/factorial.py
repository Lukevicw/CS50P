def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
factor = (int(input("Factorial of: ")))
print(factorial(factor))