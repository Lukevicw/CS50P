import re

email = input("What's your email?")





if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #Can be there once, or not at all (qpofqnop)?

#if re.search(r"^\w+@\w+\.(com|edu)|gov|org)$", email, re.IGNORECASE)
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(eu$)
#if re.search(r"^[^@]+@[^@}+\.edu$", email):
    print("Valid")
else:
    print("Invalid")