#Ask user for input
speech = input("Say something and I'll slow it down: ")

#Remove whitespace
speech = speech.strip()

#Put dots between words
print(speech.replace(" ", "..."))