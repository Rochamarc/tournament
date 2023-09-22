from classes.person import Person

class Coach(Person):
    def __init__(self, id: int, name: str, nationality: str, birth: int):
        super().__init__(name, nationality, birth)
        self.id = id 

    def __repr__(self):
        return f"Coach({self.name})"

    def __str__(self):
        return f"Coach({self.name})"