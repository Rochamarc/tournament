from controllers.base_controller import BaseController
from alive_progress import alive_it

class ClubClassController(BaseController):
    
    @classmethod
    def insert_club_classes(cls, club_classes: list[str]) -> None:
        
        for club_class in alive_it(club_classes):
            cls.insert_register(
                cls.get_query('insert','club_classes','club_classes'),
                [club_class]
            )