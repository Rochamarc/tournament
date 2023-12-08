class Formation:
    """
    Class that generates and manipulates lists with Player Objects

    ...

    Methods
    -------
    starting_eleven(squad: list)
        Make a list to fit Club.start_eleven
    backups(starting_eleven: list)
        Make a list to fit Club.bench
    select_keepers(squad: list)
        Select the goalkeepers in the squad
    select_backs(squad: list)
        Select the defensive players in the squad
    select_mids(squad: list)
        Select the midfielders in the squad
    select_fronts(squad: list)
        Select the attackers in the squad
    sorted_by_overall(players: list, reverse=False)
        Sort a list of players based on his overall
    """

    @classmethod
    def starting_eleven(cls, squad: list) -> list:
        """Add players to a list based on player's overall
        
        Parameters
        ----------
        squad : list
            A list of Player Object
        
        Returns
        -------
            A list containing 11 players
            1 Keeper
            2 Center Back
            1 Left Back
            1 Right Back
            3 Midfielders
            3 Forwards
        """

        starting_eleven = []

        # only use reverse on the first one to use the pop method
        starting_eleven.append( cls.sorted_by_overall(cls.select_keepers(squad), reverse=True).pop() ) 
        starting_eleven +=  cls.sorted_by_overall(cls.select_backs(squad))[0:4] 
        starting_eleven +=  cls.sorted_by_overall(cls.select_mids(squad))[0:3] 
        starting_eleven +=  cls.sorted_by_overall(cls.select_fronts(squad))[0:3] 

        return starting_eleven
    
    @staticmethod
    def backups(squad: list, starting_eleven: list) -> list:
        """Add players to a list based on the players that are not in starting_eleven

        Parameters
        ----------
        squad : list
            A list of Player Objects
        starting_eleven : list
            A list with eleven Player Objects
        
        Returns
        -------
            A list that match de difference between squad and starting_eleven
        """
        
        return [ player for player in squad if player not in starting_eleven ]
    
    @classmethod
    def select_keepers(cls, squad: list) -> list:
        """Select goalkeepers 

        Parameters
        ----------
        squad : list
            A list of Player Object
        
        Returns
        -------
            A list of players that have Player.position = 'GK'
        """ 
    
        return [ player for player in squad if player.position == 'GK' ]
    
    @classmethod
    def select_backs(cls, squad: list) -> list:
        """Select defensive players

        Parameters
        ----------
        squad : list
            A list of Player Object
        
        Returns
        -------
            A list of players that have Player.position = CB, RB or LB
        """ 

        return [ player for player in squad if player.position in ['CB','RB','LB'] ]
    
    @classmethod
    def select_mids(cls, squad: list) -> list:
        """Select midifielder players

        Parameters
        ----------
        squad : list
            A list of Player Object
        
        Returns
        -------
            A list of players that have Player.position = DM, CM, AM, LM or RM
        """ 

        return [ player for player in squad if player.position in ['DM','CM','AM', 'LM', 'RM'] ]
    
    @classmethod
    def select_fronts(cls, squad: list) -> list:
        """Select attacking players

        Parameters
        ----------
        squad : list
            A list of Player Object
        
        Returns
        -------
            A list of players that have Player.position = CF, SS or WG
        """ 

        return [ player for player in squad if player.position in ['CF','SS','WG'] ]
    
    @classmethod
    def sorted_by_overall(cls, players: list, reverse=False) -> list:
        """Sort the players based on Player.overall

        Parameters
        ----------
        players : list
            A list of Player Objects
        reverse : bool
            A bool that define the order of the sorting
            False = highest to lowest
            True = lowest to highest

        Returns
        -------
            A sorted list of Player Objects
        """

        players = sorted(players, key=lambda player: player.overall, reverse=reverse)
        return players

if __name__ == "__main__":
    pass 
    '''
    ceara = Club()
    ceara.start_eleven = formation.starting_eleven(ceara.squad)
    ceara.bench = formation.backups(ceara.squad, ceara.start_eleven)
    '''