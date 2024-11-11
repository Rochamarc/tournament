class Person:
    def __init__(self, name: str, nationality: str, birth: int):
        self.__name = name
        self.__nationality = nationality
        self.__birth = birth

    @property
    def nationality(self):
        return self.__nationality
    
    @property
    def name(self):
        return self.__name

    @property
    def birth(self):
        return self.__birth