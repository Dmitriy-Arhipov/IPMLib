class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1
