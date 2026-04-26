# stage2_menu.py

patients = []

while True:
    print("\n1. Add Patient\n2. View Patients\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        age = input("Age: ")
        patients.append((name, age))
    elif choice == '2':
        for p in patients:
            print(p)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
