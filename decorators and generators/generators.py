def number_generator():
    yield 1
    yield 2
    yield 3

gen = number_generator()

for num in gen:
    print(num)
