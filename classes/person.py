class Person:
    def __init__(self, name: str, nationality: str, birth: int):
        self.__name = name
        self.nationality = nationality
        self.__birth = birth

    @property
    def name(self):
        return self.__name

    @property
    def birth(self):
        return self.__birth