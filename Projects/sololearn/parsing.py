data = "From stephen.marquard@uct.ac.za Sat Jan   5  09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos) #starting from at sign
print(sppos)

host = data[atpos+1 : sppos] #up to but not including
print(host)