from db.base_controller import BaseController
import mysql.connector

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
    def insert_skills(cls, skills_data: list) -> None:
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

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()                               

        for skill in skills_data:   
            if len(skill) == 4:
                query = cls.get_insert_query('insert_gk_skills')
            else:
                query = cls.get_insert_query('insert_skills')
            
            cursor.execute(query, skill)
        
        conn.commit()
        conn.close()