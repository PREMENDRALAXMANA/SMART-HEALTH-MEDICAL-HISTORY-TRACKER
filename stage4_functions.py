# stage4_functions.py

records = []

def add_record():
    name = input("Name: ")
    age = int(input("Age: "))
    records.append({"name": name, "age": age})

def display():
    for r in records:
        print(r)

while True:
    print("\n1.Add 2.Display 3.Exit")
    ch = input()

    if ch == '1':
        add_record()
    elif ch == '2':
        display()
    else:
        break
