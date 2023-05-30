txt = input("Write a sentence: ")
lst = txt.split()

longest = "s"

for words in lst:
    if len(words) > len(longest):
        longest = words
    else:
        continue
print(longest)