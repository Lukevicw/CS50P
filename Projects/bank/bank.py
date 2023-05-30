#Prompt for input
sentence = input("Say your greeting!:")
sentence = sentence.lower()

if("hello" in sentence):
    print("$0")
elif(sentence.startswith("h")):
    print("$20")
else:
    print("$100")