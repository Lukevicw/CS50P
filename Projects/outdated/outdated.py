months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def testing():

    while True:
        try:
            while True:
                date = input("What's the date?: ")
                if ("/" not in date) and ("," not in date):
                    continue
                elif ("/" in date) and (("a" in date) or ("e" in date) or ("u" in date)):
                    continue
                else:
                    date = date.replace(",", "").replace("/", " ")
                    date = date.split()
                    if date[1] in months:
                        continue
                    else:
                        day = int(date[1])
                        year = int(date[2])

                        if date[0] in months and (day >= 1) and (day <=31):
                            month = 1 + int(months.index(date[0]))
                            print(f"{year}" + "-" + f"{month:02}" + "-" + f"{day:02}")
                            break
                        elif date[0] not in months and (day >= 1) and (day <=31):
                            month = int(date[0])
                            if (month > 12):
                                continue
                            else:
                                print(f"{year}" + "-" + f"{month:02}" + "-" + f"{day:02}")
                                break

        except ValueError:
            break
        finally:
            break



run_once = 0
while True:
    if run_once < 1:
        testing()
        run_once += 1
    else:
        break

#testing()