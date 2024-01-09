from db.base_controller import BaseController

class ClubsController(BaseController):
    """
    Class that manage the tournament.clubs table

    ...

    Methods
    -------
    select_id_name()
        Select all club's id and name
    select_id()
        Select all club's id
    select_serie_a_clubs(season: str)
        Select all clubs by serie a by season
    select_serie_b_clubs(season: str)
        Select all clubs by serie b by season
    select_serie_c_clubs(season: str)
        Select all clubs by serie c by season
    """
    
    @classmethod
    def select_id_name_class(cls) -> list[set]:
        """Select club's id, name & club_class

        Returns
        -------
            A list of lists with: id, name, club_class
        """

        return cls.select_register(cls.get_query('select','select_id_name_from_clubs'))
    
    @classmethod
    def select_id(cls) -> list[set]:
        """Select id from clubs

        Returns
        -------
            A list of lists with: id
        """

        res = cls.select_id_name_class()
        
        return [ r[0] for r in res ]

    @classmethod
    def select_serie_a_clubs(cls, season: str) -> list[set]:
        """Select all clubs that belongs to Serie A division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """

        return cls.select_register(cls.get_query('select','select_serie_a_clubs'), [season])

    @classmethod
    def select_serie_b_clubs(cls, season: str) -> list[set]:
        """Select all clubs that belongs to Serie B division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """

        return cls.select_register(cls.get_query('select','select_serie_b_clubs'), [season])    

    @classmethod
    def select_serie_c_clubs(cls, season: str) -> list[set]:
        """Select all clubs that belongs to Serie C division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """

        return cls.select_register(cls.get_query('select','select_serie_c_clubs'), [season])


    @classmethod
    def select_club_by_id(cls, id: int) -> list[set]:
        """Select a club by his id

        Parameters
        ----------
        id : int
            A int value that refers to club's id
        
        Returns
        -------
            A list of set with club: id, name, country
        """

        return cls.select_register(cls.get_query('select','select_club_by_id'), [id])
    
if __name__ == "__main__":
    print(ClubsController().select_serie_a_clubs())