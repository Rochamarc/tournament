from random import randint 

class Stadium:

    def __init__(self, name, location, capacity=None, club_owner=None):
        self.id = None
        self.name = name 
        self.location = location # City, Country ex: Manchester, UK
        self.club_owner = club_owner 
        if not capacity:
            self.capacity = randint(10_000, 50_000)
        else:
            self.capacity = capacity

    def __repr__(self):
        return f'Stadium({self.name})'

    def get_info(self):
        return f"\nName: {self.name}\nLocation: {self.location}\nCapacity: {self.capacity}\nOwner: {self.club_owner}\n"

    @property
    def data(self):

        return [ self.name, self.location, self.capacity, self.club_owner ]