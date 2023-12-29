class Stadium:
    """
    A class that represents a Football/Soccer Stadium

    ...

    Attributes
    ----------
    name : str
        The name of the Stadium
    country : str
        Stadium country
    city : str
        Stadium city
    capacity : int
        The maximum capacity of audience supported by the stadium
    """

    def __init__(self, name: str, country: str, city: str, capacity: int):
        self.name = name
        self.country = country
        self.city = city
        self.capacity = capacity
        
    def __repr__(self) -> str:
        return f'Stadium({self.name})'