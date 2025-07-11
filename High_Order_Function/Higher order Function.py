#Get Length of Each Word
#map()
"""
words = ["data", "engineer", "python", "map"]
lengths = list(map(lambda word: len(word), words))
print(lengths)"""

#duble every number
"""
nums = [10, 20, 30, 40]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)"""

#flat map()
data = [[1, 2], [3, 4], [5]]
# flatMap  using list comprehension
flat = [x for sublist in data for x in sublist]
print(flat)  