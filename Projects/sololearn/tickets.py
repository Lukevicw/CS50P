total = 0
passengers = 0
while passengers < 5:
    age = int(input())
    passengers +=1
    if age <=3:
        continue
    else:
        total += 100


print(total)