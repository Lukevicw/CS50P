import csv


students = []


with open("studentshouse.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        students.append({"name": line["name"], "home": line["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")