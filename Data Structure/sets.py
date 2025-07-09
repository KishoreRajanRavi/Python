"""s = {1, 2, 3}

s.add(4)           # Add element
s.remove(2)        # Remove element (error if not found)
s.discard(5)       # Remove safely (no error if not found)
print(len(s))      # Number of elements

"""
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference