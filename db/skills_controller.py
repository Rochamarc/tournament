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
        
    @classmethod
    def select_skills(cls, season: str) -> list[set]:
        """Select a list of skills_data

        Parameters
        ----------
        season : str
            A string value with valid season 
        
        Returns
        -------
            A list of sets with all skills data. last arg is player_id
        """

        return cls.select_register(cls.get_query('select', 'select_skills_by_season'), [season])
    
    @classmethod
    def select_last_skills(cls, season: str) -> list[set]:
        """Select the last skills inserted from tournament.skills

        Returns
        -------
            A list with 30 length containing [
            positioning,
            reflexes,
            diving,
            standing_tackle,
            physical,
            passing,
            dribbling,
            long_shot,
            finishing,
            player_id
            ]
        """

        return cls.select_register(cls.get_query('select', 'select_last_skills'), [season])