import matplotlib.pyplot as plt

# Sample data
names = ["Prem", "Rahul", "Anu"]
bp = [120, 140, 130]
ages = [20, 22, 21]

# Bar Chart (BP)
plt.figure()
plt.bar(names, bp)
plt.title("Blood Pressure of Patients")
plt.xlabel("Patients")
plt.ylabel("BP")
plt.show()

# Line Chart (Age)
plt.figure()
plt.plot(names, ages, marker='o')
plt.title("Age Trend")
plt.xlabel("Patients")
plt.ylabel("Age")
plt.show()

# Pie Chart (City Distribution)
cities = ["Vizag", "Hyderabad"]
count = [2, 1]

plt.figure()
plt.pie(count, labels=cities, autopct='%1.1f%%')
plt.title("City Distribution")
plt.show()
