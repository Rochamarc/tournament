from classes.person import Person

class Coach(Person):
    """
    A class that represents a Football/Soccer Coach

    ...

    Attributes
    ----------
    id :  int
        Unique value the representes each coach
    name : str
        The name of the coach
    nationality : str
        The nationality from the coach
    birth : int
        The birth year of the coach
    """

    def __init__(self, id: int, name: str, nationality: str, birth: int):
        super().__init__(name, nationality, birth)
        self.id = id 

    def __repr__(self):
        return f"Coach({self.name})"

    def __str__(self):
        return f"Coach({self.name})"