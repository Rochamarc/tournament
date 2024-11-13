from controllers.base_controller import BaseController

class ClubClassController(BaseController):
    
    @classmethod
    def insert_club_classes(cls, club_classes: list[str]) -> None:
        
    
        cls.insert_registers(
            cls.get_query('insert','club_classes','club_classes'),
            club_classes,
            complex=False
        )