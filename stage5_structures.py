# stage5_structures.py

patients = []

def add_patient():
    patient = {
        "id": len(patients) + 1,
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "conditions": list(input("Conditions (comma separated): ").split(","))
    }
    patients.append(patient)

def search_by_condition(cond):
    for p in patients:
        if cond in p["conditions"]:
            print(p)

add_patient()
add_patient()
search_by_condition(input("Search condition: "))
