class Stadium:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        
    def __repr__(self) -> str:
        return 'Stadium({})'.format(self.name)