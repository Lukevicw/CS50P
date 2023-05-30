#Prompt for the Great Question
answer = input("What is the answer to THE GREAT QUESTION?:").strip().lower()
answer = answer.replace(" ", "")
answer = answer.replace("-", "")

if answer == "fortytwo":
    print("Yes")
elif answer == "42":
    print("Yes")
else:
    print("No")