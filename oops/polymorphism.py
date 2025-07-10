class Cat:
    def sound(self):
        print("Cat says Meow!")

class Dog:
    def sound(self):
        print("Dog says Bark!")

# Polymorphic function
def make_animal_sound(animal):
    animal.sound()

# Create objects
c = Cat()
d = Dog()

make_animal_sound(c)  # Meow!
make_animal_sound(d)  # Bark!
