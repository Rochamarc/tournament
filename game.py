from random import choice, randint 
from base_game import BaseGame
from classes.player import Player
from classes.club import Club
from classes.stadium import Stadium

from decision_maker import simple_decision

# TODO change overall as int for decisions 

class Game(BaseGame):
    """
    Class that deals with Game Simulation, generates data and makes game decisions automatically

    ...
    Methods
    -------
    start()
        Start a match
    move(attack_club: Club, defense_club: Club, field_part: str, sender=None)
        Runs a move decisions
    player_decision(field_part=None)
        Make a player decision based on field part
    move_decision(attacker: Player, defensor: Player)
        Calculates a move sucess
    select_player_on_field(club: Club, field_part: str)
        Select a player based on his field part
    select_position_by_field(field_part: str)
        Select a player position by field part
    select_player(club: Club, player_position: str)
        Select a player based on his position and club
    finish(midfielder: Player, attacker: Player, club_finish: Club)
        Sucessfull finish
    subs(club: Club)
        Make a substitution
    add_a_goal(club: Club, attacker: Player)
        Add a goal to a club and attacker
    check_for_sub_club(club: Club)
        Check number of subs by club
    check_number_subs(n_sub: int)
        Calculates a substitution sucess
    select_club_by_home_away(club: Club)
        Return a club based on club
    select_number_of_subs_by_home_away(club: Club)
        Return home_subs or away_subs
    sub_options(club: Club)
        Select substitutes players options
    remove_one_sub(club: Club)
        Decrease a home_subs or away_subs
    set_options(player_position: str, bench: list)
        Select a list of players for position
    decision(player_overall: int)
        Calculates a decision sucess
    check_subs(n_subs: int)
        Calculates n_subs
    move_info(self, field_part: str, club_possession: Club, other_club: Club, sender: Player, keep_ball_possession: bool)
        Formulate a dict with move information
    invert_ball_possession(self, club_possession: Club, other_club: Club)
        Invert ball possession between clubs
    """
    
    def __init__(self, home: Club, away: Club, competition: str, competition_id: int, 
                 season: str, match_round: int, stadium: Stadium, ticket: int = 50):
        
        # Instantiate BaseGame variables
        super().__init__(home, away, season, stadium, competition, competition_id, ticket)

        self.home = home 
        self.away = away 
        self.competition = competition
        self.season = season 
        self.match_round = match_round
        self.stadium = stadium

        # i think this lists have to be copies
        self.home_players = self.home.start_eleven
        self.home_bench = self.home.bench

        self.away_players = self.away.start_eleven
        self.away_bench = self.away.bench

        self.add_players_on_logs()

    def start(self) -> dict:
        """Initialize a match start

        Returns
        -------
            A dict with all the game stats, movements & information
        """

        time = 0
        move_info = self.move(self.home, self.away, 'middle')

        while time < 180:
            # This is the ninety minutes simulation part 

            # Games doenst have more of seven goals
            five_goals = self.home_goal == 5 or self.away_goal == 5
            if five_goals: 
                break 
            
            move_info = self.move(move_info['club_possession'], move_info['other_club'], move_info['field_part'], move_info['sender'])
            
            # make the game have more passes
            if not move_info['keep_ball_possession'] : time += 1

        # update logs numbers
        self.update_scoreboard_on_logs()
        self.update_goals_on_logs()
        self.update_winner_on_logs()
        
        # player stats
        self.update_player_matches_on_field()
        self.check_for_goals_conceded()
        self.check_for_clean_sheets()

        return self.logs 
    
    def move(self, attack_club: Club, defense_club: Club, field_part: str, sender: Player=None) -> dict:
        """Makes decisions & calculates movements about the game and generates data
        
        Parameters
        ----------
        attack_club : Club
            Club with ball possession
        defense_club : Club
            Club that will handle defense
        field_part : str
            Field part that the ball is running
        sender : Player
            Player that have the ball. If sender is None that means that the game is gonna start or after a goal
        
        Returns
        -------
            self.move_info()
        """

        # TODO make the game have way more passes 

        keep_ball_possession =  False 

        # Define an attacker
        attacker = sender or self.select_player(attack_club)

        # Define an defensor
        defensor = self.select_player_on_field(defense_club, field_part)
        
        # Declare variables
        sender, club_possession, other_club = None, None ,None
        
        # This will be used in advance block
        destiny = choice(['back', 'middle', 'front'])
        
        # Defines a decision of the player with the ball
        player_decision = self.player_decision(field_part) 
        
        if player_decision == 'keep_ball_possession':
            # Keep ball possession
            # send to another player and keep the field
            # Here the attack club is making a move
            # The defense and the defensor are here to make the opposite
            
            # attack_move = 'pass'
            field_part = field_part

            keep_ball_possession = True

            # update for the pass
            self.update_game_stats_on_logs('passes', attack_club.name)
            self.update_player_stats_on_logs('passes', attacker)
            self.update_player_stats('passes', attacker)
            
            # check if the pass is sucess full
            f_move = self.move_decision(attacker, defensor, 'pass')

            # check for a foul to update on logs
            if not simple_decision(defensor.standing_tackle):
                self.update_game_stats_on_logs('fouls', attack_club.name)
                
                self.update_player_stats_on_logs('fouls', defensor)
                self.update_player_stats('fouls_committed', defensor)

            if f_move is False:
                # not sucessfull pass
                # keep the field part and invert the ball possession
                
                # basic method to separate a interception from a wrong pass
                # doesnt affect the game if dynamic, just the logs data
                
                interception = bool(randint(0,1))
                if interception:
                    # interception
                    self.update_game_stats_on_logs('interceptions', defense_club.name)

                    self.update_player_stats_on_logs('intercepted_passes', defensor)
                    self.update_player_stats('intercepted_passes', defensor)
                else:
                    # wrong pass
                    self.update_game_stats_on_logs('wrong passes', attack_club.name)
                    
                    self.update_player_stats_on_logs('wrong_passes', attacker)
                    self.update_player_stats('wrong_passes', attacker)
                    
                # invert ball possession
                # changes what alredy has been set
                club_possession, other_club = self.invert_ball_possession(attack_club, defense_club)
                sender = defensor
            else:
                # define info needed to insert on move
                club_possession, other_club = attack_club, defense_club
                sender = self.select_player_on_field(attack_club, field_part)
        
        elif player_decision == 'advance':
            # Make an attack move

            if field_part == 'back':
                destiny = choice(['middle','front'])
            else:
                destiny = 'front'
            
            # attack_move = choice(['pass','projection'])
            sender = self.select_player_on_field(attack_club, destiny)

            self.update_game_stats_on_logs('passes', attack_club.name)

            self.update_player_stats_on_logs('passes', attacker)
            self.update_player_stats('passes', attacker)

            f_move = self.move_decision(attacker, defensor, choice(['pass','projection'])) 

            if f_move is False:
                # this is the defense sucess
                # failed pass or projection

                defense_move = choice(['tackle','ball_steal'])

                # this could also have a wrong pass & interception
                if defense_move == 'tackle':
                    # Tackle
                    self.update_game_stats_on_logs('tackles', defense_club.name)

                    self.update_player_stats_on_logs('tackles', defensor)
                    self.update_player_stats('tackles', defensor)

                else: 
                    # Ball Steal              
                    self.update_game_stats_on_logs('stolen_balls', defense_club.name)

                    self.update_player_stats_on_logs('stolen_balls', defensor)
                    self.update_player_stats('stolen_balls', defensor)

                # invert ball possession
                club_possession, other_club = self.invert_ball_possession(attack_club, defense_club)
                sender = defensor 
            
            else:
                # Pass 
                self.update_game_stats_on_logs('passes', attack_club.name)

                self.update_player_stats('passes', attacker)

                # keep the ball possession
                # change the field_part to destiny
                field_part = destiny
                club_possession, other_club = attack_club, defense_club
                
        
        else:
            # take_a_risk
            keeper = self.select_player(defense_club, player_position='goalkeeper')
            # attack_move = 'finish'

            # i can decrease the attacker chance based on the part of the field 
            # that he is shooting passing a decrease_attacker_chance = 0 and adding
            # to the value of the attacker decision 

            # check for goalkeeper attacking
            if attacker.position == 'GK':
                self.update_player_stats_on_logs('passes', attacker)
                self.update_player_stats('passes', attacker)
                
                self.update_game_stats_on_logs('passes', attack_club.name)
                
                attacker = self.select_player(attack_club, player_position='goalkeeper', unless='GK')

            f_shot = choice(['shot','long_shot'])
            f_move = self.move_decision(attacker, keeper, f_shot)

            if f_move is False:
                ''' Defense or kick out '''

                field_part = 'back'
                sender = keeper 

                # Define for a defense or a kick out
                # to update the logs
                if simple_decision(keeper.overall):
                    self.update_game_stats_on_logs('saves', defense_club.name)

                    self.update_game_stats_on_logs('shots on target', attack_club.name)
                    self.update_player_stats('shots_on_target', attacker)
                    
                    # check for difficult defense
                    difficult_defense = bool(randint(0,1))

                    if difficult_defense:
                        self.update_player_stats('difficult_defenses', keeper)
                        self.update_player_stats_on_logs('difficult_defenses', keeper)                
                    else:
                        self.update_player_stats_on_logs('defenses', keeper)
                        self.update_player_stats('defenses', keeper)

                else:
                    # kick out
                    self.update_game_stats_on_logs('shots', attack_club.name)
                    self.update_player_stats('shots', attacker)
            else:
                # club's overall
                attack_club_overall = attack_club.overall
                
                decision = simple_decision(attacker.overall) and simple_decision(attack_club_overall)

                if decision:
                    # Goal
                    
                    # update attacking team move
                    midfielder =  self.select_player(attack_club, player_position='midfielder')
                    self.finish(midfielder, attacker, attack_club)
                    self.update_game_stats_on_logs('shots on target', attack_club.name)
                    
                    # ball on the central circle
                    field_part = 'middle'
                    
                    # change sender to defensor
                    sender = self.select_player(defense_club, player_position='attacker') 
            
            # outside goal if block
            club_possession, other_club = self.invert_ball_possession(attack_club, defense_club)
                
        
        # Make a substitution
        self.check_for_sub_club(attack_club)

        return self.move_info(field_part, club_possession, other_club, sender, keep_ball_possession)
    
    def move_info(self, field_part: str, club_possession: Club, other_club: Club, sender: Player, keep_ball_possession: bool) -> dict:
        """Defines a dict with move information

        Parameters
        ----------
        field_part : str
            A string containig part of the field where the ball is
        club_possession : Club
            A club object that has the ball
        other_club : Club
            A club object that is defending
        sender : Player
            A player that has the ball
        keep_ball_possession : bool
            A bool value for the ball possession
        
        Returns
        -------
            A dict with information about that moment in the game
        """

        return {
            'field_part': field_part,
            'club_possession': club_possession,
            'other_club': other_club,
            'sender': sender,
            'keep_ball_possession': keep_ball_possession
        }

    def invert_ball_possession(self, club_possession: Club, other_club: Club) -> list:
        """Invert clubs order

        Parameters
        ----------
        club_possession : Club
            A club object that has the ball
        other_club : Club
            A club object that is defending
        
        Returns
        -------
            An inverted list of the club objects
        """

        return [ other_club, club_possession ]
    
    def player_decision(self, field_part: str) -> str:
        """Simulates a decision that can be made by a player by his field part

        Parameters
        ----------
        field_part : str
            Part of the field that the player is

        Returns
        -------
            A string that matches a player decision 
        """
        
        # lets increase the chance of keep ball possession and advance 
        # to try to make my data has way more passes

        if field_part == 'front':
            # 3 chances of 4 to keep ball possesion
            return choice(['keep_ball_possesion','keep_ball_possession','keep_ball_possession', 'take_a_risk'])
        # 3/6 chances of ball_possession, 2/6 chances of advance 1/6 chances of take_a_risk
        return choice(['keep_ball_possession', 'keep_ball_possession','keep_ball_possession', 'advance', 'advance', 'take_a_risk'])

    def move_decision(self, attacker: Player, defensor: Player, move: str) -> bool:
        """Make a bool decision about the movement

        Parameters
        ----------
        attacker : Player
           Attacking player that will provides his overall
        defensor : Player
            Defensor player that will provides his overall
        move : str
            A string containing a football move

        Returns
        -------
            A bool based on the denial of defensor decision and a true attacker decision
        """

        if move in ['pass','projection']:
            # TODO 
            # pass, projection and interception to
            # skills table 
            # for now i'm using defensor's overall

            return not simple_decision(defensor.overall) and simple_decision(attacker.passing)
        elif move == 'shot':
            return not simple_decision(defensor.diving) and simple_decision(attacker.finishing)
        elif move == 'long_shot':
            return not simple_decision(defensor.positioning) and simple_decision(attacker.long_shot)
        else:
            return not simple_decision(defensor.overall) and simple_decision(attacker.overall)  

    def select_player_on_field(self, club: Club, field_part: str) -> Player:
        """Select a random player based on his field part 
        
        Parameters
        ----------
        club : Club
            A Club Object
        field_part : str
            A string that will set the position

        Returns
        -------
            A Player object
        """

        return self.select_player(club, player_position=self.select_position_by_field(field_part))

    def select_position_by_field(self, field_part: str) -> str:
        """Select a player football role based on field_part

        Parameters
        ----------
        field_part : str
            A string containing a field_part

        Returns
        -------
            A string containing a football role 
        """

        if field_part == 'back':
            return 'attacker'
        if field_part == 'middle':
            return 'midfielder'
        
        return 'defender'

    def select_player(self, club: Club, player_position: str = None, unless: str = None) -> Player:
        """Select a player by a specific position
        
        Parameters
        ----------
        club : Club
            A Club object that will set the list of players to be selected
        player_position : str
            A string with a player position to be included or excluded from the selection.
            ex: If the unless parameter are gonna be used, pass the name of the position, like: 
            'goalkeeper','midfielder'. 
        unless : str
            A string containing an acronym for a position to be excluded from selection.
            ex: 'GK' for goalkeeper, 'CB' for center back.
        
        Raises
        ------
        Exception : if the unless parameters are true and player_position if false,
            player_position can be True and unless False but not the other way
        NameError : if club doesnt't belongs to match self.home or self.away
        Returns
        -------
            A Player Object
        """

        if unless and not player_position:
            raise Exception("If you pass a unless parameter you're have to pass a player_position parameter.")
        
        if club == self.home:
            start_eleven = self.home_players
        elif club == self.away:
            start_eleven = self.away_players 
        else:
            raise NameError('Club {} does not match {} or {}'.format(club, self.home.name, self.away.name))

        #   check for player position and unless clause
        #   if both are true the use want exclude a position
        #   if player position are true and unless false the user want a specific position 
        #   if both are false the user want any player

        if player_position and unless:
            options = [ player for player in start_eleven if player.position not in self.positions[player_position] ]
        elif not (player_position and unless):
            options = start_eleven
        else:
            options = [ player for player in start_eleven if player_position in self.positions[player_position] ]


        return choice(options)


    def finish(self, assistant: Player, finisher: Player, club_finish: Club) -> True:
        """Update base_game logs & attributes

        Parameters
        ----------
        assistant : Player
            A Player Object that make the assistance
        finisher : Player
            A Player Object that make the finish
        club_finish : Club
            Club Object that have the assistant and finisher
        
        Returns
        -------
            A True boolean
        """

        assist = choice([True,False]) # defines if the goal have an assist

        self.add_a_goal(club_finish, finisher)

        # Add stats to logs
        self.update_game_stats_on_logs('goals', club_finish.name)

        self.update_player_stats_on_logs('goals', finisher)
        self.update_player_stats('goals', finisher)

        if assist: 
            self.update_player_stats_on_logs('assists', assistant)
            self.update_player_stats('assists', assistant)

        return True
    
    def subs(self, club: Club) -> bool:
        """Make a substitution and updates the base_game logs

        Parameters
        ----------
        club : Club
            A Club Object that will make the substitution

        Returns
        -------
            A bool based on the sucessfullness of the substitution
        """
        
        # Defines s_check, startin, bench, n_subs
        sub_opt = self.sub_options(club) 
        s_check, starting = sub_opt[0], sub_opt[1]
        bench, home_away = sub_opt[2], sub_opt[3]
        
        # Select the player that is going to leave
        player_out = choice(starting) 

        # Select the possible players based on the position
        options = self.set_options(player_out.position, bench)
        
        if s_check and options:
            # Select player the will enter the field
            player_in = choice(options) 
            
            # Remove subed player from starting eleven & bench
            starting.remove(player_out) 
            bench.remove(player_in) 
            
            # Add player to starting eleven
            starting.append(player_in) 
            
            # Remove one from subb
            self.remove_one_sub(club)
            
            # add player_in on the logs
            self.add_player_on_logs(home_away, player_in)
            
            return True
        return False 
    
    def add_a_goal(self, club: Club, attacker: Player) -> None:
        """Update base_game logs & attributes related to goals

        Parameters
        ----------
        club : Club
            A Club Object that score the goal
        attacker : Player
            A Player Object that score the goal
        
        Returns
        -------
            None
        """
        
        if club == self.home:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1
            return None 
        
        self.away_goal += 1
        self.away_player_goals[attacker] += 1
        return None

    def check_for_sub_club(self, club: Club) -> bool:
        """Check for the number of subs 
        
        Parameters
        ----------
        club : Club
            A Club Object

        Returns
        -------
            A boolean
        """
        
        # get the same club by pointing to self.home or self.away
        # maybe this can be excluded without worries
        
        n_subs = self.select_club_number_of_subs_by_home_away(club)

        if self.check_number_subs(n_subs):
            # here i make a substituiton
            self.subs(club)
            return True 
        return False 

    def check_number_subs(self, n_sub: int) -> bool:
        """Check if number of subs is greater than zero

        Parameters
        ----------
        n_sub : int
            An integer of number of subs

        Returns
        -------
            A random boolean for number of subs greater than zero 
        """

        if n_sub > 0:  
            return choice([True, False]) 
        return False

    def select_club_number_of_subs_by_home_away(self, club: Club) -> int:
        """Point to a club subs based on club parameter

        Parameters
        ----------
        club : Club
            A Club Object
        
        Returns
        -------
            An integer with the number of subs 
        """
        
        return self.home_subs if club == self.home else self.away_subs

    def sub_options(self, club) -> list:
        """Select a list of players that can be subbed

        Parameters
        ----------
        club : Club
            A Club Object
        
        Returns
        -------
            A list with Player Objects that are'n in Club().start_eleven
        """
        
        if club == self.home:
            return [ self.check_subs(self.home_subs), self.home_players, self.home_bench, 'home' ]
        return [self.check_subs(self.away_subs), self.away_players, self.away_bench, 'away']

    def remove_one_sub(self, club: Club) -> None:
        """Decrease one home_subs or away_subs class attribute

        Parameters
        ----------
        club : Club
            A Club Object
        
        Returns
        -------
            None
        """
        
        if club == self.home : self.home_subs -= 1
        if club == self.away : self.away_subs -= 1        

    def set_options(self, player_position: str, bench: list) -> list:
        """Select a list of players by position

        Parameters
        ----------
        player_position : str
            A string with player's position
        bench : list
            A list of bench players
        
        Returns
        -------
            A list with bench players
        """
        
        positions = self.positions.copy()
        del positions['goalkeeper']
        
        for key, item in positions.items():
            if player_position in item:
                return [ b for b in bench if b.position in positions[key] ]
        return None
    
    def check_subs(self, n_subs) -> bool:
        """Check for a sub based on number of subs

        Parameters
        ----------
        n_subs : int
            An integer containing number of subs
        
        Returns
        -------
            A bool
        """
        
        return n_subs > 0


    def __repr__(self) -> str:
        return 'Game({} x {})'.format(self.home, self.away)