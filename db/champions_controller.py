from db.base_controller import BaseController

class ChampionsController(BaseController):
    """
    Class that manage the tournament.champíons table

    ...

    Methods
    -------

    insert_champion(season: str, division_id, club_id: int)
        Insert a league title to a club
    """

    @classmethod
    def insert_champion(cls, season: str, division_id: int, club_id: int, competition_name: str, division_name: str) -> None:
        """Insert a league title to a club

        Parameters
        ----------
        season : str
            A string that refers to the season won by club
        division_id : int
            A int value that refers to division id
        club_id : int
            A int value that referes to club id
        competition_name : str
            A string value containing competition's name
        division_name : str
            A string value containing division's name

        Raises
        ------
            Exception if there's a champion saved in database on the competition, division and season

        Returns
        -------
            None
        """

        if cls.check_champion(season, competition_name, division_name):
            raise Exception("DataBase error: there's alredy an champions with this season: {}, on competition: {} {}.".format(season, competition_name, division_name))


        data = [season, division_id, club_id]
        return cls.insert_register(cls.get_query('insert','insert_champions'), data)

    @classmethod
    def check_champion(cls, season: str, competition_name: str, division_name: str) -> bool:
        """Check on database if are an champion with this season, divison and season
        
        Parameters
        ----------
        season : str
            A string with season value
        competition_name : str
            A string containing the competition's name
        division_name : str
            A string containing the division's name

        Returns
        -------
            True if there's a champion inserted on database and a False for not 
        """

        data = cls.check_register(cls.get_query('check', 'check_champions'), [competition_name, division_name, season])
        if data:
            return True
        return False