amount = 0

while amount < 50:
   print("Amount due:", 50 - amount)
   coin = int(input("Insert coin: "))
   if coin == 25:
      amount += 25
   elif coin == 10:
      amount += 10
   elif coin == 5:
      amount += 5
   else:
      amount += 0

while amount >= 50:
   if amount == 50:
      print("Change owed:", amount - 50)
      break
   else:
      print("Change owed:", amount - 50)
      break
