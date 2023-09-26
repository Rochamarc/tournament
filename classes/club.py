class Club:
    def __init__(self, id: int, name: str, country: str):
        self.id = id
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()

        self.squad = []
        self.start_eleven = []
        self.bench = []

    def __repr__(self):
        return f"Club({self.name})"
    
    def add_to_squad(self, *values: list):
        self.cast += values