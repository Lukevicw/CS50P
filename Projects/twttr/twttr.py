tweet = input("Input: ")
replace = { 'A': '','E': '','I': '', 'O': '','U': '','a': '', 'e': '','i': '','o': '','u': ''}

for key, value in replace.items():
    tweet = tweet.replace(key, value)

print("Output: ", tweet)