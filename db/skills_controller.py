from db.base_controller import BaseController

class SkillsController(BaseController):
    """
    Class that manage the tournament.players
    
    ...

    Methods
    -------
    insert_skills(skills_data: list)
        Insert a list of tournament.skills in database

    """
    
    @classmethod
    def insert_skills(cls, skills_data: list, season: str) -> None:
        """Insert a list of overall data into tournament.overall
        
        Parameters
        ----------
        overall_data : list
            A list of list containing
            positioning: int, reflexes: int, diving: int, standing_tackle: int, physical: int, 
            passing: int, dribbling: int, long_shot: int, finishing: int, player_id: int
        
        Returns
        -------
            None
        """

        for skill in skills_data:   
            skill.insert(0, season) # insert season at data

            if len(skill) == 5:
                query = cls.get_query('insert', 'insert_gk_skills')
            else:
                query = cls.get_query('insert', 'insert_skills')
            
            cls.insert_register(query, skill)