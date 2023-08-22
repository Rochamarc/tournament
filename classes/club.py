class Club:
    def __init__(self,name: str,country: str, club_class: str, total_budget: int, salary_budget: int):
        self.id = None
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()

        self.club_class = club_class

        self.total_budget = total_budget
        self.salary_budget = salary_budget

        self.cast = []
        self.start_eleven = []
        self.bench = []

    def __repr__(self):
        return f"Club({self.name})"
    
    def add_to_cast(self, *values: list):
        self.cast += values