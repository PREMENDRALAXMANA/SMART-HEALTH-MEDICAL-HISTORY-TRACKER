# stage3_vitals.py

vitals = []

while True:
    name = input("Enter Patient Name: ").strip().lower()
    bp = input("Enter BP: ")
    sugar = input("Enter Sugar Level: ")

    vitals.append({"name": name, "bp": bp, "sugar": sugar})

    ch = input("Add more? (y/n): ")
    if ch == 'n':
        break

# Search
search = input("Search Patient: ").lower()

for v in vitals:
    if v["name"] == search:
        print(v)
