# Parent class
class Parent:
    def show_message(self):
        print("This is the Parent class")

# Child class inherits from Parent
class Child(Parent):
    def display(self):
        print("This is the Child class")

# Create object of Child
obj = Child()
obj.show_message()   # inherited from Parent
obj.display()        # from Child
