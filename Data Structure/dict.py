# Dictionary Example in Python

# Creating a dictionary of student details
student = {
    "name": "Kishore",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("Name:", student["name"])
print("Course:", student["course"])


student["marks"] = 90


student["email"] = "kishore@example.com"


print("\nUpdated Student Info:")
for key, value in student.items():
    print(key, ":", value)
