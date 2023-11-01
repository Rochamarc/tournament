class Stadium:
    """
    A class that represents a Football/Soccer Stadium

    ...

    Attributes
    ----------
        name : str
            The name of the Stadium
        location : str
            The location of the stadium
        capacity : int
            The maximum capacity of audience supported by the stadium
    """

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        
    def __repr__(self) -> str:
        return 'Stadium({})'.format(self.name)