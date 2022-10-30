class Person:
    def __init__(self, name, nationality, age):
        self.id = None
        self.name = name
        self.nationality = nationality
        self.age = age

    def increase_age(self):
        self.age += 1