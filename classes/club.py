class Club:
    def __init__(self,id: int, name: str,country: str, club_class: str, total_budget: int, salary_budget: int):
        self.id = id
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()

        self.cast = []
        self.start_eleven = []
        self.bench = []

    def __repr__(self):
        return f"Club({self.name})"
    
    def add_to_cast(self, *values: list):
        self.cast += values