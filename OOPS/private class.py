class Company:
    class _Employee:  # "Private-like" inner class (by convention)
        def __init__(self, name):
            self.name = name

        def display(self):  # Public method
            print("Employee Name:", self.name)

    def create_employee(self, name):
        emp = self._Employee(name)
        emp.display()

# Create Company object
c1 = Company()
c1.create_employee("Mezba")
