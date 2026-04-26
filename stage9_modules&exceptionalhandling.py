# main.py

from utils.validators import validate_age

try:
    age = int(input("Enter age: "))
    validate_age(age)
except ValueError as e:
    print("Error:", e)
