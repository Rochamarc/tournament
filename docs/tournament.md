# Table of Contents

* [configure](#configure)
* [game](#game)
  * [Game](#game.Game)
    * [start](#game.Game.start)
    * [move](#game.Game.move)
    * [player\_decision](#game.Game.player_decision)
    * [move\_decision](#game.Game.move_decision)
    * [select\_player\_on\_field](#game.Game.select_player_on_field)
    * [select\_position\_by\_field](#game.Game.select_position_by_field)
    * [select\_player](#game.Game.select_player)
    * [finish](#game.Game.finish)
    * [subs](#game.Game.subs)
    * [check\_for\_sub\_club](#game.Game.check_for_sub_club)
    * [check\_number\_subs](#game.Game.check_number_subs)
    * [select\_club\_by\_home\_away](#game.Game.select_club_by_home_away)
    * [select\_club\_number\_of\_subs\_by\_home\_away](#game.Game.select_club_number_of_subs_by_home_away)
    * [sub\_options](#game.Game.sub_options)
    * [remove\_one\_sub](#game.Game.remove_one_sub)
    * [set\_options](#game.Game.set_options)
    * [decision](#game.Game.decision)
    * [check\_subs](#game.Game.check_subs)
* [base\_game](#base_game)
  * [BaseGame](#base_game.BaseGame)
    * [\_\_init\_\_](#base_game.BaseGame.__init__)
    * [add\_players\_on\_logs](#base_game.BaseGame.add_players_on_logs)
    * [add\_player\_on\_logs](#base_game.BaseGame.add_player_on_logs)
    * [update\_scoreboard\_on\_logs](#base_game.BaseGame.update_scoreboard_on_logs)
    * [update\_goals\_on\_logs](#base_game.BaseGame.update_goals_on_logs)
    * [update\_winner\_on\_logs](#base_game.BaseGame.update_winner_on_logs)
    * [update\_player\_stats\_on\_logs](#base_game.BaseGame.update_player_stats_on_logs)
    * [update\_game\_stats\_on\_logs](#base_game.BaseGame.update_game_stats_on_logs)
* [logs\_helper](#logs_helper)
  * [LogsHandler](#logs_helper.LogsHandler)
    * [get\_game\_stats](#logs_helper.LogsHandler.get_game_stats)
    * [prepare\_game\_stats\_logs\_to\_db](#logs_helper.LogsHandler.prepare_game_stats_logs_to_db)
    * [prepare\_game\_logs\_to\_db](#logs_helper.LogsHandler.prepare_game_logs_to_db)
    * [prepare\_championships\_logs\_to\_db](#logs_helper.LogsHandler.prepare_championships_logs_to_db)
* [helper](#helper)
  * [ClassConstructor](#helper.ClassConstructor)
    * [players](#helper.ClassConstructor.players)
    * [clubs](#helper.ClassConstructor.clubs)
    * [stadiums](#helper.ClassConstructor.stadiums)
    * [add\_players\_to\_clubs](#helper.ClassConstructor.add_players_to_clubs)
    * [define\_formation](#helper.ClassConstructor.define_formation)
    * [define\_schedule](#helper.ClassConstructor.define_schedule)
    * [prepare\_games](#helper.ClassConstructor.prepare_games)
* [main](#main)
  * [p](#main.p)
  * [players](#main.players)

<a id="configure"></a>

# configure

<a id="game"></a>

# game

<a id="game.Game"></a>

## Game Objects

```python
class Game(BaseGame)
```

<a id="game.Game.start"></a>

#### start

```python
def start() -> dict
```

Initialize a match, return the game logs

<a id="game.Game.move"></a>

#### move

```python
def move(attack_club, defense_club, field_part, sender=None)
```

Dict with info of move
{ 'destiny': '', 'club_possession': '', 'other_club': '', 'sender': '' }

<a id="game.Game.player_decision"></a>

#### player\_decision

```python
def player_decision(field_part=None) -> str
```

Return a decision that can be made by a player

<a id="game.Game.move_decision"></a>

#### move\_decision

```python
def move_decision(attacker, defensor) -> bool
```

Based on attacker and defensor overall make a decision, but the defensor have advantage

<a id="game.Game.select_player_on_field"></a>

#### select\_player\_on\_field

```python
def select_player_on_field(club, field_part: str)
```

Return a player based on field part

<a id="game.Game.select_position_by_field"></a>

#### select\_position\_by\_field

```python
def select_position_by_field(field_part: str) -> str
```

Return a position based on the field_part argument

<a id="game.Game.select_player"></a>

#### select\_player

```python
def select_player(club, player_position)
```

Return a player from the club start eleven

<a id="game.Game.finish"></a>

#### finish

```python
def finish(midfielder, attacker, club_finish)
```

Represents a sucessfull finish. Update the stats on logs

<a id="game.Game.subs"></a>

#### subs

```python
def subs(club) -> bool
```

Will make a sub if everything goes well return True

<a id="game.Game.check_for_sub_club"></a>

#### check\_for\_sub\_club

```python
def check_for_sub_club(club) -> bool
```

Receive a club as argument and return true if the sub will happen

<a id="game.Game.check_number_subs"></a>

#### check\_number\_subs

```python
def check_number_subs(n_sub: int) -> None
```

Return True or False if the n of subs is greater than 0

<a id="game.Game.select_club_by_home_away"></a>

#### select\_club\_by\_home\_away

```python
def select_club_by_home_away(club)
```

Return a club pointer based on home or away

<a id="game.Game.select_club_number_of_subs_by_home_away"></a>

#### select\_club\_number\_of\_subs\_by\_home\_away

```python
def select_club_number_of_subs_by_home_away(club)
```



<a id="game.Game.sub_options"></a>

#### sub\_options

```python
def sub_options(club) -> list
```

Return the s_check, starting, bench & home_away

<a id="game.Game.remove_one_sub"></a>

#### remove\_one\_sub

```python
def remove_one_sub(club) -> None
```

Remove one sub

<a id="game.Game.set_options"></a>

#### set\_options

```python
def set_options(player_position, bench)
```

Return a list of players for a position that matches the player_position

<a id="game.Game.decision"></a>

#### decision

```python
def decision(p_overall) -> bool
```

Retrun True if player overall is greater then a random between (1,100)

<a id="game.Game.check_subs"></a>

#### check\_subs

```python
def check_subs(n_subs) -> bool
```

returns True if the team still have subs left

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

<a id="base_game.BaseGame.__init__"></a>

#### \_\_init\_\_

```python
def __init__(home, away, season, stadium, ticket)
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
def add_player_on_logs(home_away: str, player) -> None
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
def update_player_stats_on_logs(stats: str, player)
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

<a id="base_game.BaseGame.update_game_stats_on_logs"></a>

#### update\_game\_stats\_on\_logs

```python
def update_game_stats_on_logs(stat: str, home_away: str)
```

Increase by one the stat on logs['game_stats'][home_away][stats]

Parameters
----------
stat : str
    The stat that will be increased
home_away : str
    Club's name

Returns
-------
    None

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

    [ win, loss, draw, home_goals, away_goals, goals_diff, club_id, season ]

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
	[ id, name, nationality, birth, position, height, weight, foot, overall, club_id ]

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
	[ stadium_name, stadium_location, stadium_capacity ] 

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
                  season: int) -> list[Game]
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

<a id="main"></a>

# main

<a id="main.p"></a>

#### p

get from db

<a id="main.players"></a>

#### players

transform into objects

