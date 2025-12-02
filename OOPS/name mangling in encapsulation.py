class Student:
    def __init__(self):
        self.__name = "Mezba"  # Private variable (name mangled)

    def show_name(self):
        return self.__name

# Create object
s1 = Student()
# Access using public method
print("Name via method:", s1.show_name())  # Works

# Direct access (will cause error)
# print(s1.__name)  This gives: AttributeError

# Access using name mangling
print("Accessing with mangled name:", s1._Student__name)  # Works
