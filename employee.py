class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Overload + operator
    def __add__(self, other):
        return self.salary + other.salary

    # Overload - operator
    def __sub__(self, other):
        return self.salary - other.salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# Create Employee objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 40000)

# Display employees
emp1.display()
emp2.display()

# Using overloaded operators
print("\nCombined Salary:", emp1 + emp2)
print("Salary Difference:", emp1 - emp2)