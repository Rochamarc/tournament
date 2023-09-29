class Formation:
    @classmethod
    def starting_eleven(cls, squad: list) -> list:
        ''' Return the starting eleven squad
            Only in 4-3-3 for now 
        '''

        starting_eleven = []

        # only use reverse on the first one to use the pop method
        starting_eleven.append( cls.sorted_by_overall(cls.select_keepers(squad), reverse=True).pop() ) 
        starting_eleven.append( cls.sorted_by_overall(cls.select_backs(squad))[0:4] )
        starting_eleven.append( cls.sorted_by_overall(cls.select_mids(squad))[0:3] )
        starting_eleven.append( cls.sorted_by_overall(cls.select_fronts(squad))[0:3] )

        return starting_eleven
    
    @staticmethod
    def backups(squad: list, starting_eleven: list) -> list:
        ''' Return the bench players '''
        return [ player for player in squad if player not in starting_eleven ]
    
    @classmethod
    def select_keepers(cls, squad: list) -> list: 
        return [ player for player in squad if player.position == 'GK' ]
    
    @classmethod
    def select_backs(cls, squad: list) -> list:
        return [ player for player in squad if player.position in ['CB','RB','LB'] ]
    
    @classmethod
    def select_mids(cls, squad: list) -> list:
        return [ player for player in squad if player.position in ['DM','CM','AM', 'LM', 'RM'] ]
    
    @classmethod
    def select_fronts(cls, squad: list) -> list:
        return [ player for player in squad if player.position in ['CF','SS','WG'] ]
    
    @classmethod
    def sorted_by_overall(cls, players: list, reverse = False) -> list:
        players = sorted(players, key=players.overall, reverse=reverse)
        return players