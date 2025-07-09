"""t = (10, 20, 30, 40)

print(t[0])        # Access by index → 10
print(t[-1])       # Last item → 40
print(len(t))      # Length → 4
print(30 in t)     # Membership test → True

for item in t:
    print("looping",item)
"""

# Packing
t = ("Kishore", 21, "Trainee")

# Unpacking
name, age, role = t
print(name)  # Kishore
print(age)   # 21
print(role)  # Trainee
