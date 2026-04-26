# models/patient.py

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# usage
p1 = Patient("Prem", 20)
p1.display()
