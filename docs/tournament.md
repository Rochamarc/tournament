# Table of Contents

* [data\_helper](#data_helper)
  * [prepare\_player\_stats\_to\_db](#data_helper.prepare_player_stats_to_db)
* [data\_manipulation](#data_manipulation)
  * [tuple\_to\_list](#data_manipulation.tuple_to_list)
  * [change\_to\_a](#data_manipulation.change_to_a)
  * [change\_to\_b](#data_manipulation.change_to_b)
  * [change\_to\_c](#data_manipulation.change_to_c)
  * [fomrmulate\_clubs\_to\_simple\_cup](#data_manipulation.fomrmulate_clubs_to_simple_cup)
  * [formulate\_clubs\_to\_championships](#data_manipulation.formulate_clubs_to_championships)
  * [relegate\_brazillian\_tournament](#data_manipulation.relegate_brazillian_tournament)
  * [apply\_reduction](#data_manipulation.apply_reduction)
* [cup](#cup)
  * [clubs\_data](#cup.clubs_data)
  * [players\_data](#cup.players_data)
  * [game\_data](#cup.game_data)
* [game](#game)
  * [Game](#game.Game)
    * [start](#game.Game.start)
    * [move](#game.Game.move)
    * [move\_info](#game.Game.move_info)
    * [invert\_ball\_possession](#game.Game.invert_ball_possession)
    * [player\_decision](#game.Game.player_decision)
    * [move\_decision](#game.Game.move_decision)
    * [select\_player\_on\_field](#game.Game.select_player_on_field)
    * [select\_position\_by\_field](#game.Game.select_position_by_field)
    * [select\_player](#game.Game.select_player)
    * [finish](#game.Game.finish)
    * [subs](#game.Game.subs)
    * [add\_a\_goal](#game.Game.add_a_goal)
    * [check\_for\_sub\_club](#game.Game.check_for_sub_club)
    * [check\_number\_subs](#game.Game.check_number_subs)
    * [select\_club\_by\_home\_away](#game.Game.select_club_by_home_away)
    * [select\_club\_number\_of\_subs\_by\_home\_away](#game.Game.select_club_number_of_subs_by_home_away)
    * [sub\_options](#game.Game.sub_options)
    * [remove\_one\_sub](#game.Game.remove_one_sub)
    * [set\_options](#game.Game.set_options)
    * [decision2](#game.Game.decision2)
    * [check\_subs](#game.Game.check_subs)
    * [decision](#game.Game.decision)
* [data\_generator](#data_generator)
  * [get\_skill\_by\_position](#data_generator.get_skill_by_position)
  * [get\_skill\_by\_class](#data_generator.get_skill_by_class)
  * [generate\_players\_skills](#data_generator.generate_players_skills)
* [main\_api](#main_api)
* [insert\_functions](#insert_functions)
  * [check\_yes\_no](#insert_functions.check_yes_no)
  * [check\_for\_season](#insert_functions.check_for_season)
* [configure](#configure)
* [helper](#helper)
  * [ClassConstructor](#helper.ClassConstructor)
    * [players](#helper.ClassConstructor.players)
    * [clubs](#helper.ClassConstructor.clubs)
    * [stadiums](#helper.ClassConstructor.stadiums)
    * [add\_players\_to\_clubs](#helper.ClassConstructor.add_players_to_clubs)
    * [define\_formation](#helper.ClassConstructor.define_formation)
    * [define\_schedule](#helper.ClassConstructor.define_schedule)
    * [prepare\_games](#helper.ClassConstructor.prepare_games)
    * [prepare\_cup\_games](#helper.ClassConstructor.prepare_cup_games)
    * [prepare\_clubs](#helper.ClassConstructor.prepare_clubs)
  * [CupHelper](#helper.CupHelper)
    * [invert\_confronts](#helper.CupHelper.invert_confronts)
    * [sort\_simple\_cup\_confronts](#helper.CupHelper.sort_simple_cup_confronts)
    * [run\_cup\_phase](#helper.CupHelper.run_cup_phase)
* [logs\_helper](#logs_helper)
  * [LogsHandler](#logs_helper.LogsHandler)
    * [get\_player\_stats](#logs_helper.LogsHandler.get_player_stats)
    * [get\_game\_stats](#logs_helper.LogsHandler.get_game_stats)
    * [prepare\_game\_stats\_logs\_to\_db](#logs_helper.LogsHandler.prepare_game_stats_logs_to_db)
    * [prepare\_game\_logs\_to\_db](#logs_helper.LogsHandler.prepare_game_logs_to_db)
    * [prepare\_championships\_logs\_to\_db](#logs_helper.LogsHandler.prepare_championships_logs_to_db)
    * [prepare\_cup\_game\_logs\_to\_db](#logs_helper.LogsHandler.prepare_cup_game_logs_to_db)
    * [prepare\_knock\_out\_logs\_to\_db](#logs_helper.LogsHandler.prepare_knock_out_logs_to_db)
* [data\_formulation](#data_formulation)
  * [pretty\_print](#data_formulation.pretty_print)
  * [print\_stars](#data_formulation.print_stars)
* [cup\_game](#cup_game)
  * [CupGame](#cup_game.CupGame)
    * [start](#cup_game.CupGame.start)
    * [check\_winner](#cup_game.CupGame.check_winner)
    * [add\_first\_leg\_goals](#cup_game.CupGame.add_first_leg_goals)
    * [penalty\_shootout](#cup_game.CupGame.penalty_shootout)
    * [penalty\_shooting](#cup_game.CupGame.penalty_shooting)
    * [check\_penalties\_winner](#cup_game.CupGame.check_penalties_winner)
* [main](#main)
* [base\_game](#base_game)
  * [BaseGame](#base_game.BaseGame)
    * [\_\_init\_\_](#base_game.BaseGame.__init__)
    * [add\_players\_on\_logs](#base_game.BaseGame.add_players_on_logs)
    * [add\_player\_on\_logs](#base_game.BaseGame.add_player_on_logs)
    * [update\_scoreboard\_on\_logs](#base_game.BaseGame.update_scoreboard_on_logs)
    * [update\_goals\_on\_logs](#base_game.BaseGame.update_goals_on_logs)
    * [update\_penalties\_on\_logs](#base_game.BaseGame.update_penalties_on_logs)
    * [update\_winner\_by\_penalties\_on\_logs](#base_game.BaseGame.update_winner_by_penalties_on_logs)
    * [update\_winner\_on\_logs](#base_game.BaseGame.update_winner_on_logs)
    * [update\_player\_stats\_on\_logs](#base_game.BaseGame.update_player_stats_on_logs)
    * [update\_player\_stats](#base_game.BaseGame.update_player_stats)
    * [update\_game\_stats\_on\_logs](#base_game.BaseGame.update_game_stats_on_logs)
    * [prepare\_player\_data\_dict](#base_game.BaseGame.prepare_player_data_dict)
    * [check\_for\_clean\_sheets](#base_game.BaseGame.check_for_clean_sheets)
    * [check\_for\_goals\_conceded](#base_game.BaseGame.check_for_goals_conceded)
    * [update\_player\_matches\_on\_field](#base_game.BaseGame.update_player_matches_on_field)
* [tournament](#tournament)
  * [run\_league](#tournament.run_league)

<a id="data_helper"></a>

# data\_helper

<a id="data_helper.prepare_player_stats_to_db"></a>

#### prepare\_player\_stats\_to\_db

```python
def prepare_player_stats_to_db(player_stats: dict, season: str,
                               game_id: int) -> list[list]
```

Prepare a list of data to insert into tournament.stats schema

Parameters
----------
player_stats : dict
    Stats from Game.logs['stats'] format
season : str
    A str with season 
game_id : int
    A integer of the id from the game

Returns
-------
    A list of list with tournament.stats data

<a id="data_manipulation"></a>

# data\_manipulation

<a id="data_manipulation.tuple_to_list"></a>

#### tuple\_to\_list

```python
def tuple_to_list(data: list) -> list[list]
```

Convert a list of sets or tuples to list objects

Parameters
----------
data : list
    A set of data

Returns
-------
    A python list objects of the inserted data

<a id="data_manipulation.change_to_a"></a>

#### change\_to\_a

```python
def change_to_a(data: list) -> list[list]
```

Change the division id to 1

Parameters
----------
data : list
    A list of lists with club's information

Returns
-------
    The data list with updated id value

<a id="data_manipulation.change_to_b"></a>

#### change\_to\_b

```python
def change_to_b(data: list) -> list[list]
```

Change the division id to 2

Parameters
----------
data : list
    A list of lists with club's information

Returns
-------
    The data list with updated id value

<a id="data_manipulation.change_to_c"></a>

#### change\_to\_c

```python
def change_to_c(data: list) -> list[list]
```

Change the division id to 3

Parameters
----------
data : list
    A list of lists with club's information

Returns
-------
    The data list with updated id value

<a id="data_manipulation.fomrmulate_clubs_to_simple_cup"></a>

#### fomrmulate\_clubs\_to\_simple\_cup

```python
def fomrmulate_clubs_to_simple_cup(data_1: list, data_2: list) -> list
```

Formulate club's id for sort confronts

Paramters
---------
data_1 : list
    A list of lists, sets or tuples with club_id data
data_2 : list
    A list of lists, sets or tuples with club_id data

Returns
-------
    A one dimentional list combined by the two data lists

Raises
------
Exception
    If the final data length is odd

<a id="data_manipulation.formulate_clubs_to_championships"></a>

#### formulate\_clubs\_to\_championships

```python
def formulate_clubs_to_championships(data_1: list, data_2: list,
                                     data_3: list) -> list
```

Change promoted, relegated and remains clubs to next season

Parameters
----------
data_1 : list
    A list of data of clubs that remains in the division
data_2 : list
    A list of data (promoted or relegated) that change divison
data_3 : list
    A list of data (promoted or relegated) that change divison. ps:Use an empy list if this data will not be usefull

Returns
-------
    A list of of data with len = numbers of clubs per division

<a id="data_manipulation.relegate_brazillian_tournament"></a>

#### relegate\_brazillian\_tournament

```python
def relegate_brazillian_tournament(championships_data: list, next_season: str,
                                   division: str) -> dict
```

Manipulate championships to to separate clubs that will stay in the
serie a division to the relegated

Parameters
----------
championships_data : list
    A list of sets with [ club_id, division_id ]
next_season : int
    Int value for the next season 
division : str
    A value for division: serie_a, serie_b, or serie_c 

Returns
-------
    A dict with { remains: [ [club_id, division_id, next_season] ], relegated: [ [club_id, serie_b_division_id, next_season] ] }

<a id="data_manipulation.apply_reduction"></a>

#### apply\_reduction

```python
def apply_reduction(value: int) -> int
```

Reduce value by multiplying the value for
0.25

Parameters
----------
value : int
    An int value from 55 to 99

Returns
-------
    A convert int value from result of value * 0.25

<a id="cup"></a>

# cup

<a id="cup.clubs_data"></a>

#### clubs\_data

Get clubs data

<a id="cup.players_data"></a>

#### players\_data

Get players from database

<a id="cup.game_data"></a>

#### game\_data

Define the condronts

<a id="game"></a>

# game

<a id="game.Game"></a>

## Game Objects

```python
class Game(BaseGame)
```

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

<a id="game.Game.start"></a>

#### start

```python
def start() -> dict
```

Initialize a match start

Returns
-------
    A dict with all the game stats, movements & information

<a id="game.Game.move"></a>

#### move

```python
def move(attack_club: Club,
         defense_club: Club,
         field_part: str,
         sender: Player = None) -> dict
```

Makes decisions & calculates movements about the game and generates data

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

<a id="game.Game.move_info"></a>

#### move\_info

```python
def move_info(field_part: str, club_possession: Club, other_club: Club,
              sender: Player, keep_ball_possession: bool) -> dict
```

Defines a dict with move information

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

<a id="game.Game.invert_ball_possession"></a>

#### invert\_ball\_possession

```python
def invert_ball_possession(club_possession: Club, other_club: Club) -> list
```

Invert clubs order

Parameters
----------
club_possession : Club
    A club object that has the ball
other_club : Club
    A club object that is defending

Returns
-------
    An inverted list of the club objects

<a id="game.Game.player_decision"></a>

#### player\_decision

```python
def player_decision(field_part: str) -> str
```

Simulates a decision that can be made by a player by his field part

Parameters
----------
field_part : str
    Part of the field that the player is

Returns
-------
    A string that matches a player decision

<a id="game.Game.move_decision"></a>

#### move\_decision

```python
def move_decision(attacker: Player, defensor: Player, move: str) -> bool
```

Make a bool decision about the movement

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

<a id="game.Game.select_player_on_field"></a>

#### select\_player\_on\_field

```python
def select_player_on_field(club: Club, field_part: str) -> Player
```

Select a random player based on his field part

Parameters
----------
club : Club
    A Club Object
field_part : str
    A string that will set the position

Returns
-------
    A Player object

<a id="game.Game.select_position_by_field"></a>

#### select\_position\_by\_field

```python
def select_position_by_field(field_part: str) -> str
```

Select a player football role based on field_part

Parameters
----------
field_part : str
    A string containing a field_part

Returns
-------
    A string containing a football role

<a id="game.Game.select_player"></a>

#### select\_player

```python
def select_player(club: Club,
                  player_position: str = None,
                  unless: str = None) -> Player
```

Select a player by a specific position

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

<a id="game.Game.finish"></a>

#### finish

```python
def finish(assistant: Player, finisher: Player, club_finish: Club) -> True
```

Update base_game logs & attributes

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

<a id="game.Game.subs"></a>

#### subs

```python
def subs(club: Club) -> bool
```

Make a substitution and updates the base_game logs

Parameters
----------
club : Club
    A Club Object that will make the substitution

Returns
-------
    A bool based on the sucessfullness of the substitution

<a id="game.Game.add_a_goal"></a>

#### add\_a\_goal

```python
def add_a_goal(club: Club, attacker: Player) -> None
```

Update base_game logs & attributes related to goals

Parameters
----------
club : Club
    A Club Object that score the goal
attacker : Player
    A Player Object that score the goal

Returns
-------
    None

<a id="game.Game.check_for_sub_club"></a>

#### check\_for\_sub\_club

```python
def check_for_sub_club(club: Club) -> bool
```

Check for the number of subs

Parameters
----------
club : Club
    A Club Object

Returns
-------
    A boolean

<a id="game.Game.check_number_subs"></a>

#### check\_number\_subs

```python
def check_number_subs(n_sub: int) -> bool
```

Check if number of subs is greater than zero

Parameters
----------
n_sub : int
    An integer of number of subs

Returns
-------
    A random boolean for number of subs greater than zero

<a id="game.Game.select_club_by_home_away"></a>

#### select\_club\_by\_home\_away

```python
def select_club_by_home_away(club: Club) -> Club
```

Select home or away class attribute based on club

Parameters
---------- 
club : Club
    A Club Object  

Returns
-------
    A Club Object

<a id="game.Game.select_club_number_of_subs_by_home_away"></a>

#### select\_club\_number\_of\_subs\_by\_home\_away

```python
def select_club_number_of_subs_by_home_away(club: Club) -> int
```

Select home_subs or away_subs class attribute based on club

Parameters
----------
club : Club
    A Club Object

Returns
-------
    An integer with the number of subs

<a id="game.Game.sub_options"></a>

#### sub\_options

```python
def sub_options(club) -> list
```

Select a list of players that can be subbed

Parameters
----------
club : Club
    A Club Object

Returns
-------
    A list with Player Objects that are'n in Club().start_eleven

<a id="game.Game.remove_one_sub"></a>

#### remove\_one\_sub

```python
def remove_one_sub(club: Club) -> None
```

Decrease one home_subs or away_subs class attribute

Parameters
----------
club : Club
    A Club Object

Returns
-------
    None

<a id="game.Game.set_options"></a>

#### set\_options

```python
def set_options(player_position: str, bench: list) -> list
```

Select a list of players by position

Parameters
----------
player_position : str
    A string with player's position
bench : list
    A list of bench players

Returns
-------
    A list with bench players

<a id="game.Game.decision2"></a>

#### decision2

```python
def decision2(p_overall) -> bool
```

Calculates a decision based on players overall

Parameters
----------
p_overall : int
    An integer with players overall

Returns
-------
    A bool

<a id="game.Game.check_subs"></a>

#### check\_subs

```python
def check_subs(n_subs) -> bool
```

Check for a sub based on number of subs

Parameters
----------
n_subs : int
    An integer containing number of subs

Returns
-------
    A bool

<a id="game.Game.decision"></a>

#### decision

```python
def decision(p_overall: int, num_trials: int = 1) -> bool
```

Calculates a decision based on players overall

Parameters
----------
p_overall : int
    An integer with players overall

Returns
-------
    A bool

<a id="data_generator"></a>

# data\_generator

<a id="data_generator.get_skill_by_position"></a>

#### get\_skill\_by\_position

```python
def get_skill_by_position(position: str, club_class: str) -> list[int]
```

Define a list of values based on player position

Parameters
----------
position : str
    Argument that defines how his skills are gonna be calculated
club_class : str
    A 1 length string value that referes to A, B, C or D

Returns
-------
    A list of integer values

<a id="data_generator.get_skill_by_class"></a>

#### get\_skill\_by\_class

```python
def get_skill_by_class(club_class: str) -> int
```

Generate data based on value on club clubs

Parameters
----------
club_class : str
    A 1 length string value that referes to A, B, C or D

Returns 
-------
    A random int value

<a id="data_generator.generate_players_skills"></a>

#### generate\_players\_skills

```python
def generate_players_skills(season: str) -> None
```

Generate skill data for players and insert into database

Parameters
----------
season : str
    A string with season value for the skill

Returns
-------
    None

<a id="main_api"></a>

# main\_api

<a id="insert_functions"></a>

# insert\_functions

<a id="insert_functions.check_yes_no"></a>

#### check\_yes\_no

```python
def check_yes_no(other_values: list = [])
```

Asks for an input and check if the input is Y or n

Parameters
----------
other_values : list
    A default empty lists, add other valid values for input 

Raises
------
    ValueError if the value passed on input is invalid

Return
------
    A string containing a valid value for 'yes' or 'no'

<a id="insert_functions.check_for_season"></a>

#### check\_for\_season

```python
def check_for_season()
```

Asks for an input and check if the input is a string value that can be
convert as an integer and if the value has length of 4

Raises
------
    ValueError if the len is diff than 4
    TypeError if the value cannot be convert to an integer

Returns
-------
    A string containing a valid value for season

<a id="configure"></a>

# configure

<a id="helper"></a>

# helper

<a id="helper.ClassConstructor"></a>

## ClassConstructor Objects

```python
class ClassConstructor()
```

Class focused in transform db data into objects

    ...

    Methods
    -------
    players(players_data: list)
        Instantiate players
   	clubs(clubs_data: list)
		Instantiate clubs
	stadiums(stadiums_data: list)
		Instantiate stadiums
	add_players_to_clubs(clubs: list, players: list)
		Add players to Club.squad
	define_formation(clubs: list)
		Modify Club's start_eleven and bench
	define_schedule(clubs: list)
		Generates confronts between clubs
	prepare_games(games: list, stadiums: list, competition: str, season: int)
		Instantiate games
	prepare_cup_games(games: list, competition: str, competition_id: int, season: str, phase: str, game_number: int, stadiums: list, first_leg_home_goals: int=0, first_leg_away_goals: int=0)
		Instantiate cup games
	prepare_clubs(cls, clubs_data: list, players_data: list)
		Instantiate clubs & players and configure their formation

<a id="helper.ClassConstructor.players"></a>

#### players

```python
@staticmethod
def players(players_data: list) -> list[Player]
```

Transform data into Player Objects

Parameters
----------
players_data : list
	A list of data with the following format
	[ id, name, nationality, birth, position, height, weight, foot, positioning,
	reflexes, diving, dribling, long_shot, finishing, club_id ]

Returns
-------
	A list of Player Objects constructed with the data received

<a id="helper.ClassConstructor.clubs"></a>

#### clubs

```python
@staticmethod
def clubs(clubs_data: list) -> list[Club]
```

Transform data into Club Objects

Parameters
----------
clubs_data : list
	A list of data with the following format 
	[ club_id, club_name, club_country ] 

Returns
-------
	A list of Club Objects constructed with the data received

<a id="helper.ClassConstructor.stadiums"></a>

#### stadiums

```python
@staticmethod
def stadiums(stadiums_data: list) -> list[Stadium]
```

Transform data into Stadium Objects

Parameters
----------
stadiums_data : list
	A list of data with the following format 
	[ stadium_name, stadium_country, stadium_city, stadium_capacity ] 

Returns
-------
	A list of Stadium Objects constructed with the data received

<a id="helper.ClassConstructor.add_players_to_clubs"></a>

#### add\_players\_to\_clubs

```python
@staticmethod
def add_players_to_clubs(clubs: list, players: list) -> list[Club]
```

Add players to squad according to player.club_id and club_id

Parameters
----------
clubs : list
	A list of Club Objects
players : list
	A list of Player Objects

Returns
------- 
	A list of Club Objects

<a id="helper.ClassConstructor.define_formation"></a>

#### define\_formation

```python
@staticmethod
def define_formation(clubs: list) -> None
```

Modify the Club.start_eleven & Club.bench

Parameters
----------
clubs : list
	A list of Clubs Objects That have players in Club.squad

Returns
-------
	None

<a id="helper.ClassConstructor.define_schedule"></a>

#### define\_schedule

```python
@staticmethod
def define_schedule(clubs: list) -> list[list]
```

Generates a list of confronts between two different clubs.
Each list has 2 elements a home and away team, two confronts can be
equal if their positioning in the list is inverted
ex: [team_a, team_b] , [team_b, team_a]

Parameters
----------
clubs : list 
	A list of Club Objects

Returns
-------
	A list of lists containing two clubs in each one

<a id="helper.ClassConstructor.prepare_games"></a>

#### prepare\_games

```python
@staticmethod
def prepare_games(games: list, stadiums: list, competition: str,
                  competition_id: int, season: int) -> list[Game]
```

Transform data into Game Objects

Parameters
----------
games : list
	A list of game data containing two clubs
stadiums : list
	A list of Stadiums Objects
competition : str
	Name of the competition of this games
season : int
	Season relating to this games

Returns
-------
	A list of Game Objetcs

<a id="helper.ClassConstructor.prepare_cup_games"></a>

#### prepare\_cup\_games

```python
@staticmethod
def prepare_cup_games(games: list,
                      competition: str,
                      competition_id: int,
                      season: str,
                      phase: str,
                      game_number: int,
                      stadiums: list,
                      first_leg_home_goals: int = 0,
                      first_leg_away_goals: int = 0) -> list[Game]
```

Transform data into CupGame objects

Paramters
---------
games : list
	A list of game data containing two clubs
competition : str
	Name of the competition of this games
competition_id : int
	A int value for the competition id
season : int
	Season relating to this games
phase : str
	A string value containing the phase name ex: round of 32 | round of 16 | ...
game_number : int
	A int value between 1 or 2 for the match number
stadiums : list
	A list of Stadium Objects
first_leg_home_goals : int
	A int value for the home first leg goals. Default value is 0
first_leg_away_goals : int
	A int value for the away first leg goals. Default value is 0

Returns
-------
	A list of CupGame objects

<a id="helper.ClassConstructor.prepare_clubs"></a>

#### prepare\_clubs

```python
@classmethod
def prepare_clubs(cls, clubs_data: list, players_data: list) -> list[Club]
```

Prepare clubs & players by their respective data

Parameters
----------
clubs_data : list
	A list containing clubs data
players_data : list
	A list containing players data

Returns 
-------
	A list of club objects configure and prepared to player

<a id="helper.CupHelper"></a>

## CupHelper Objects

```python
class CupHelper()
```

Class focused on dealing with cup only functions

sort_simple_cup_confronts(clubs_id: list)
	Sort clubs confronts to the Copa Do Brasil
invert_confronts(confronts: list)
	Preapre confronts for the second leg match
run_cup_phase(phase: str, match_number: int, competition_id: int, games: list)
	Runs a cup phase

<a id="helper.CupHelper.invert_confronts"></a>

#### invert\_confronts

```python
@staticmethod
def invert_confronts(confronts: list) -> list
```

Prepare data for the 2 of 2 game

Parameters
----------
confronts : list
	A list of lists containing a pair of Club Objects

Returns
-------
	A list of lists with inverted club position

<a id="helper.CupHelper.sort_simple_cup_confronts"></a>

#### sort\_simple\_cup\_confronts

```python
@staticmethod
def sort_simple_cup_confronts(clubs: list) -> list[list]
```

Groups the list into a two dimensional array with doubles random values

Parameters
----------
clubs : list
	A list containing a pair of Club objects

Returns
-------
	A list of lists with two Club objects inside of each one

<a id="helper.CupHelper.run_cup_phase"></a>

#### run\_cup\_phase

```python
@staticmethod
def run_cup_phase(phase: str, match_number: int, competition_id: int,
                  games: list) -> list
```

Run all games from a cup

Parameters
----------
phase : str
	A string with cup phase
games : list
	A list of games

<a id="logs_helper"></a>

# logs\_helper

<a id="logs_helper.LogsHandler"></a>

## LogsHandler Objects

```python
class LogsHandler()
```

Class that contains static methods to handle the logs 
generated by the BaseGame class

...

Methods
-------
get_game_stats(logs: dict, home: Club, away: Club)
    Return a formated list of Game().logs['game_stats'] from the Game().home and Game().away

prepare_game_stats_logs_to_db(logs: dict)
    Return a formated list of the Game().logs['game_stats'] 
    to be inserted in the tournament.games on Database

prepare_game_logs_to_db(logs: dict, game_stats_id: list)
    Return a formated list to be inserted in the tournament.game_stats on Database

prepare_championships_logs_to_db(logs: dict, club: int, season: int)
    Returan a formated list to be inserted in the tournament.championships on Database

<a id="logs_helper.LogsHandler.get_player_stats"></a>

#### get\_player\_stats

```python
@staticmethod
def get_player_stats(logs: dict, stat: str) -> list
```

Filter the players stats from logs

Parameters
----------
logs : dict
    Dict of data from from Game().logs
stat : str
    String the stat that you want to get from logs

Returns
-------
    A list with player and number of the stat

<a id="logs_helper.LogsHandler.get_game_stats"></a>

#### get\_game\_stats

```python
@staticmethod
def get_game_stats(logs: dict, home: Club, away: Club) -> dict
```

Return the game stats from logs

Parameters
----------
logs : dict
    The return dict from the Game().logs
home : Club
    The Club object that matches Game().home
away : Club
    The Club object that matches Game().home

Returns
-------
    Add the clubs's ids on the logs['game_stats'] 
    and return a dict with home and away game_stats

<a id="logs_helper.LogsHandler.prepare_game_stats_logs_to_db"></a>

#### prepare\_game\_stats\_logs\_to\_db

```python
@staticmethod
def prepare_game_stats_logs_to_db(logs: dict) -> list[list]
```

Convert logs dict to data to be inserted on database

Parameters
----------
logs : dict
    The Game().logs['game_stats'] with club's id inserted

Returns
-------
    A list formated with the data to be inserted in the 
    tournament.game_stats table

<a id="logs_helper.LogsHandler.prepare_game_logs_to_db"></a>

#### prepare\_game\_logs\_to\_db

```python
@staticmethod
def prepare_game_logs_to_db(logs: dict, game_stats_id: list) -> list
```

Convert logs dict to data to be inserted on database

Parameters
----------
logs : dict
    The return dict from Game().logs 
game_stats_id: list
    A list containing the database game_stats.id from the home and away club

Returns
-------
    A list formated with the data to be inserted in the 
    tournamet.game table

<a id="logs_helper.LogsHandler.prepare_championships_logs_to_db"></a>

#### prepare\_championships\_logs\_to\_db

```python
@staticmethod
def prepare_championships_logs_to_db(logs: dict, club: Club,
                                     season: str) -> list
```

Convert and prepare the logs to insert a chmapionships table

Parameters
----------
logs : dict
    The return dict from Game().logs
club : Club
    A Club Object
season : str
    The value of the season from the championship

Returns
-------
    A formated list with a data to be inserted in the 
    tournament.championships table

    /* pontos, vitorias, empates, derrotas, gols, sofridos, club_id, season */
    [ points, win, loss, draw, home_goals, away_goals, club_id, season ]

<a id="logs_helper.LogsHandler.prepare_cup_game_logs_to_db"></a>

#### prepare\_cup\_game\_logs\_to\_db

```python
@staticmethod
def prepare_cup_game_logs_to_db(game_data: list, competition_id: int,
                                home_game_stats_id: int,
                                away_game_stats_id: int) -> list
```

Prepare data list for cup games on database

Atributes
---------
game_data : list
    The default game data logs
competition_id : int
    A int value for the competition's id
home_game_stats_id : int
    A int value for the home game stats
away_game_stats_id : int
    A int value for the away game stats

Returns
-------
    The game_data attribute with competition_id, home_game_stats_id, away_game_stats_id appended to it

<a id="logs_helper.LogsHandler.prepare_knock_out_logs_to_db"></a>

#### prepare\_knock\_out\_logs\_to\_db

```python
@staticmethod
def prepare_knock_out_logs_to_db(phase: str,
                                 single_match: bool,
                                 match_number: int,
                                 game_id: int,
                                 penalties_id: int = False) -> list
```

Prepare data list for knock out table on database

Attributes
----------
phase : str
    A string with phase ex: 'round of 32', 'round of 16', 'quarter finals', 'semi finals', 'final'
single_match : bool
    A bool value for two legs or one leg
match_number : int
    Number of the match 1 of 2 or 2 of 2 case of single_match = False
game_id : int
    A int value for the game_id
penalties_id : int
    A int value for the penalties id if penalties is True

Returns
-------
    A list with [ phase, single_match, match_number, game_id, penalties_id if True ]

<a id="data_formulation"></a>

# data\_formulation

<a id="data_formulation.pretty_print"></a>

#### pretty\_print

```python
def pretty_print(data: list) -> None
```

Print database data for humans

Parameters
----------
data : list
    A list of sets of data 

Returns
-------
    None

<a id="data_formulation.print_stars"></a>

#### print\_stars

```python
def print_stars(string_value: str) -> None
```

Print a string_value between dashes and line breaker

Parameters
----------
string_value : str
    A printable string value

Returns
-------
    None

<a id="cup_game"></a>

# cup\_game

<a id="cup_game.CupGame"></a>

## CupGame Objects

```python
class CupGame(Game)
```

Class that deals with Cup Game Simulation, generates data and makes game decisions automatically
inherits from Game and BaseGame

<a id="cup_game.CupGame.start"></a>

#### start

```python
def start() -> dict
```

Initialize a match start

Returns
-------
    A dict with all the game stats, movements & information

<a id="cup_game.CupGame.check_winner"></a>

#### check\_winner

```python
def check_winner() -> bool
```

Check's if the game has a winner on second game

Returns
-------
    True if has a winner and False if it's a tie

<a id="cup_game.CupGame.add_first_leg_goals"></a>

#### add\_first\_leg\_goals

```python
def add_first_leg_goals(home_goals: int, away_goals: int) -> None
```

Add goals on logs

Parameters
----------
home_goals : int
    A integer value of home_goals
away_goals : int
    A integer value of away_goals

Returns
-------
    None

<a id="cup_game.CupGame.penalty_shootout"></a>

#### penalty\_shootout

```python
def penalty_shootout() -> None
```

Simulates a penalty shootout 5 alternate penalties for each club.
if tie, the run one shoot until one of the club misses and the other get it right

Returns
-------
    None

<a id="cup_game.CupGame.penalty_shooting"></a>

#### penalty\_shooting

```python
def penalty_shooting(shooter: Player, keeper: Player) -> bool
```

Simulate a penalty shoot

Parameters
----------
shooter : Player
    Player object shooting the penalty
keeper : Player
    Player object defending the penalty

Returns
-------
    decision between shooter and keeper

<a id="cup_game.CupGame.check_penalties_winner"></a>

#### check\_penalties\_winner

```python
def check_penalties_winner() -> Club
```

Check for a penalties winner

Returns
-------
    home if home_penalties > away_penalties or away

<a id="main"></a>

# main

<a id="base_game"></a>

# base\_game

<a id="base_game.BaseGame"></a>

## BaseGame Objects

```python
class BaseGame()
```

Class that deals with Game logs and all data inside the Game

...

Methods
-------
add_players_on_logs()
    Add players to logs['players']
add_player_on_logs(home_away: str, player: Player)
    Add one player to logs['players']
update_goals_on_logs()
    Update logs['scoreboard']
update_goals_on_logs()
    Update logs['others']['home_goals'] & logs['others']['away_goals']
update_winner_on_logs()
    Calculate winner and loser OR draw
update_player_stats_on_logs(stats: str, player: Player)
    Increase by one the player_stats on logs
update_game_stats_on_logs(stat: str, home_away: str)
    Increase by one the game_stats on logs
update_player_stats(stats: str, player: Player)
    Update stats item on logs
prepare_player_data_dict(home_players: list, away_players: list)
    Prepare dict data for player stats

<a id="base_game.BaseGame.__init__"></a>

#### \_\_init\_\_

```python
def __init__(home: Club, away: Club, season: str, stadium: Stadium,
             competition: str, competition_id: int, ticket: int)
```

This will handle all that code that have to do with the game data

<a id="base_game.BaseGame.add_players_on_logs"></a>

#### add\_players\_on\_logs

```python
def add_players_on_logs() -> None
```

Add self.home_players & self.away_players to logs['players']

Returns
-------
    None

<a id="base_game.BaseGame.add_player_on_logs"></a>

#### add\_player\_on\_logs

```python
def add_player_on_logs(home_away: str, player: Player) -> None
```

Add one player to logs['players']

Parameters
----------
home_away : str
    Club's name
player : Player
    Player Object

Returns
-------
    None

<a id="base_game.BaseGame.update_scoreboard_on_logs"></a>

#### update\_scoreboard\_on\_logs

```python
def update_scoreboard_on_logs() -> None
```

Update the scoreboard goals on logs['scoreboard']

Returns
-------
    None

<a id="base_game.BaseGame.update_goals_on_logs"></a>

#### update\_goals\_on\_logs

```python
def update_goals_on_logs() -> None
```

Update the goals on logs['others]['home_goals'] & logs['others]['away_goals']

Returns
-------
    None

<a id="base_game.BaseGame.update_penalties_on_logs"></a>

#### update\_penalties\_on\_logs

```python
def update_penalties_on_logs() -> None
```

Update the penalties on logs['others']['home_penalties'] & logs['others']['away_penalties']
ps: This adds two new values to dictionary, they don't have this two keys originaly

Returns
-------
    None

<a id="base_game.BaseGame.update_winner_by_penalties_on_logs"></a>

#### update\_winner\_by\_penalties\_on\_logs

```python
def update_winner_by_penalties_on_logs() -> None
```

Calculate the difference between self.home_penalties & self.away_penalties then update logs winner and loser

Retruns
-------
    None

<a id="base_game.BaseGame.update_winner_on_logs"></a>

#### update\_winner\_on\_logs

```python
def update_winner_on_logs() -> None
```

Calculate the difference between self.home_goals & self.away_goals then update logs winner and loser.
If the diference between self.home_goals & away_goals =0, update the logs['others']['draw'] = True and end function.

Returns
-------
    None

<a id="base_game.BaseGame.update_player_stats_on_logs"></a>

#### update\_player\_stats\_on\_logs

```python
def update_player_stats_on_logs(stats: str, player: Player)
```

Increase by one the stat on logs['player_stats'][stats][player]


Parameters
----------
stats : str
    The stat that will be increased
player : str
    Player Object that will be increased

Returns
-------
    None

<a id="base_game.BaseGame.update_player_stats"></a>

#### update\_player\_stats

```python
def update_player_stats(stats: str, player: Player, n: int = 1) -> None
```

Update stats item on logs

Parameters
----------
stats : str
    A string containing stat that will be increased
    stats options => matches, goals, assists, tackles, passes, wrong_passes, intercepted_passes, clearances, stolen_balls, clean_sheets, defenses, difficult_defenses, goals_conceded     
players : Player
    A player object 
n: int
    Value that will be added on stats

Returns
-------
    None

<a id="base_game.BaseGame.update_game_stats_on_logs"></a>

#### update\_game\_stats\_on\_logs

```python
def update_game_stats_on_logs(stat: str, club_name: str)
```

Increase by one the stat on logs['game_stats'][home_away][stats]
stats options => goals, shots, shots on target, fouls, passes, wrong passes, interceptions, tackles, stolen_balls, saves, ball possession, offsides, free kicks, penalties

Parameters
----------
stat : str
    The stat that will be increased
home_away : str
    Club's name

Returns
-------
    None

<a id="base_game.BaseGame.prepare_player_data_dict"></a>

#### prepare\_player\_data\_dict

```python
def prepare_player_data_dict(home_players: list, away_players: list) -> dict
```

Prepare player stats data

Parameters
----------
home_players : list
    Home Club squad
away_players : list
    Away Club squad

Returns
-------
    A dict with player game data for home and away players

<a id="base_game.BaseGame.check_for_clean_sheets"></a>

#### check\_for\_clean\_sheets

```python
def check_for_clean_sheets() -> None
```

Check for clean sheet and update stats for clean_sheets
to all players on stats

Returns
-------
    None

<a id="base_game.BaseGame.check_for_goals_conceded"></a>

#### check\_for\_goals\_conceded

```python
def check_for_goals_conceded()
```

Check for goals conceded and update stats for goals_conceded
to all players on stats

Returns
-------
    None

<a id="base_game.BaseGame.update_player_matches_on_field"></a>

#### update\_player\_matches\_on\_field

```python
def update_player_matches_on_field() -> None
```

Update matches from players that enter the field on self.logs['stats']

Returns
-------
    None

<a id="tournament"></a>

# tournament

<a id="tournament.run_league"></a>

#### run\_league

```python
def run_league(games: list, season: str) -> None
```

Run a full season of a league tournament

Parameters
----------
games : list
    A Game object list
season : str
    A str with season 

Returns
-------
    None

