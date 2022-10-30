from random import randint, choice

class GamesUtilitaries:
    @staticmethod
    def combat(attacker, defender):
        ''' A combat system where the defender always have the advantage '''

        _att = GamesUtilitaries.return_bool(attacker.overall)
        _def = GamesUtilitaries.return_bool(defender.overall)

        if _att and not _def:
            return attacker
        return defender

    @staticmethod 
    def finish(attacker, defender):
        ''' This simulates a shot on target where the attacker have advantage '''

        _att = GamesUtilitaries.return_bool(attacker.overall)
        _def = GamesUtilitaries.return_bool(defender.overall)

        if (_att and _def) or ((not _att) and _def):
            return "no goal" # { 'player': defender, 'defense': True }           
        return "goal" # { 'player': attacker, 'goal': True }
    
    @staticmethod
    def select_player(self, club, player_position):
        ''' Return a player from the club start eleven '''

        if club == self.home_club:
            start_eleven = self.home_players
        elif club == self.away_club:
            start_eleven = self.away_players 
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        if player_position == 'any':
            return choice(start_eleven)

        positions = {
            "goalkeeper": [ 'GK' ],
            "defender": [ 'CB', 'RB', 'LB'],
            "midfielder": [ 'DM', 'CM', 'AM'],
            "attacker": [ 'CF', 'SS', 'WG' ]
        }

        player = choice([player for player in start_eleven if player.position in positions[player_position]])

        return player 

    @staticmethod
    def return_bool(overall):
        return randint(1,99) < overall

    @staticmethod 
    def toss_a_coin(heads, tails):
        return choice([heads, tails])

    @staticmethod 
    def roll_a_dice():
        return randint(1,6)

