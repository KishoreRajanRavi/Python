# Step 1: Read from a file
"""
with open("data.txt", "r") as f:
    #content = f.read()
    content = f.readlines()

    print("📄 File Content:\n", content)
"""

# Step 2: Write to another file
"""
with open("output.txt", "w") as f:
    f.write("This is written by Kishore!\n")
    f.write("Great start in Python file handling.")"""
#append
"""
with open("data.txt", "a") as f:
    f.write("This line is added at the end.\n")"""

# Read and Write
"""
with open("data.txt", "r+") as f:
    content = f.read()
    f.write("\nAdding this after reading!")"""

# Read image
"""
with open("file handling.png", "rb") as file:
    image_data = file.read()
    print("✅ Image loaded!")
    print("File size in bytes:", len(image_data))

# Write binary data to new file
with open("file handling_copy.png", "wb") as f:
    f.write(image_data)

print("✅ Image copied successfully!")"""

import os
os.remove("demo delete.txt")
print("Successfully Deleted")


