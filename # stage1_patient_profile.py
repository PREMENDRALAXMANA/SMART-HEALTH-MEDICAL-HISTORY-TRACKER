# stage1_patient_profile.py

name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
blood_group = input("Enter Blood Group: ")
height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))
phone = input("Enter Phone Number: ")

print("\n--- Patient Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Blood Group: {blood_group}")
print(f"Height: {height} cm")
print(f"Weight: {weight} kg")
print(f"Phone: {phone}")
