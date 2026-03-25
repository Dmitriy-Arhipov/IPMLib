class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"
