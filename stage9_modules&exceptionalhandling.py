# utils/validators.py

def validate_age(age):
    if age < 0:
        raise ValueError("Invalid Age")
