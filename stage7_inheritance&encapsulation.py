# models/record.py

class Record:
    def __init__(self, id):
        self._id = id   # protected

class Patient(Record):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def display(self):
        print(f"ID: {self._id}, Name: {self.name}")

p = Patient(1, "Prem")
p.display()
