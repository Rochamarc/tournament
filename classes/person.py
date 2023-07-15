class Person:
    def __init__(self, name: str, nationality: str, age: int):
        self.id = None
        self.__name = name
        self.nationality = nationality
        self.__age = age

    def increase_age(self):
        ''' Increase the age of a player with one year'''
        self.__age += 1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
