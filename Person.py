class Person:
    count = 0
    def __init__(self, name):
        Person.count += 1
        self.name = name

    def display(self):
        print(f"Name : {self.name}")

    @classmethod
    def get_count(cls):
        return cls.count


# Create objects
p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

# Display details
p1.display()
p2.display()
p3.display()

# Display total number of Person objects created
print("Total Persons:", Person.get_count())

    