"""def number_generator():
    yield 1
    yield 2
    yield 3

gen = number_generator()

for num in gen:
    print(num)"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
print(next(gen))
print(next(gen))

