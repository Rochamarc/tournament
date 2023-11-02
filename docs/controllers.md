# Table of Contents

* [base\_controller](#base_controller)
  * [BaseController](#base_controller.BaseController)
    * [get\_select\_query](#base_controller.BaseController.get_select_query)
    * [get\_update\_query](#base_controller.BaseController.get_update_query)
    * [get\_insert\_query](#base_controller.BaseController.get_insert_query)
* [coach\_contracts\_controller](#coach_contracts_controller)
  * [CoachContractsController](#coach_contracts_controller.CoachContractsController)
    * [insert\_coach\_contracts](#coach_contracts_controller.CoachContractsController.insert_coach_contracts)
* [stadiums\_controller](#stadiums_controller)
  * [StadiumsController](#stadiums_controller.StadiumsController)
    * [select\_all\_stadiums](#stadiums_controller.StadiumsController.select_all_stadiums)
* [players\_controller](#players_controller)
  * [PlayersController](#players_controller.PlayersController)
    * [insert\_players](#players_controller.PlayersController.insert_players)
    * [select\_last\_players](#players_controller.PlayersController.select_last_players)
    * [select\_all\_players\_id](#players_controller.PlayersController.select_all_players_id)
    * [select\_players\_by\_club](#players_controller.PlayersController.select_players_by_club)
    * [select\_players\_with\_contract](#players_controller.PlayersController.select_players_with_contract)
* [championship\_controller](#championship_controller)
  * [ChampionshipsController](#championship_controller.ChampionshipsController)
    * [select\_championship\_table\_by\_club](#championship_controller.ChampionshipsController.select_championship_table_by_club)
    * [select\_championship\_table\_by\_division](#championship_controller.ChampionshipsController.select_championship_table_by_division)
    * [update\_championship\_table](#championship_controller.ChampionshipsController.update_championship_table)
* [overall\_controller](#overall_controller)
  * [OverallController](#overall_controller.OverallController)
    * [insert\_overall](#overall_controller.OverallController.insert_overall)
* [player\_contracts\_controller](#player_contracts_controller)
  * [PlayerContractsController](#player_contracts_controller.PlayerContractsController)
    * [insert\_player\_contracts](#player_contracts_controller.PlayerContractsController.insert_player_contracts)
* [clubs\_controller](#clubs_controller)
  * [ClubsController](#clubs_controller.ClubsController)
    * [select\_id\_name](#clubs_controller.ClubsController.select_id_name)
    * [select\_id](#clubs_controller.ClubsController.select_id)
    * [select\_serie\_a\_clubs](#clubs_controller.ClubsController.select_serie_a_clubs)
    * [select\_serie\_b\_clubs](#clubs_controller.ClubsController.select_serie_b_clubs)
    * [select\_serie\_c\_clubs](#clubs_controller.ClubsController.select_serie_c_clubs)
* [games\_controller](#games_controller)
  * [GamesController](#games_controller.GamesController)
    * [insert\_games\_list](#games_controller.GamesController.insert_games_list)
    * [insert\_game\_stat\_with\_id\_return](#games_controller.GamesController.insert_game_stat_with_id_return)
    * [select\_last\_id](#games_controller.GamesController.select_last_id)
* [coaches\_controller](#coaches_controller)
  * [CoachesController](#coaches_controller.CoachesController)
    * [insert\_coaches](#coaches_controller.CoachesController.insert_coaches)
    * [select\_id](#coaches_controller.CoachesController.select_id)

<a id="base_controller"></a>

# base\_controller

<a id="base_controller.BaseController"></a>

## BaseController Objects

```python
class BaseController()
```

Base class that contains every property and functions used in other controllers

<a id="base_controller.BaseController.get_select_query"></a>

#### get\_select\_query

```python
@classmethod
def get_select_query(cls, file_name: str) -> str
```

Get one query on db/queries/select

Parameters
----------
file_name : str
    Name of the file inside the path without the file extension

Returns
-------
    A string with the query in the file

Raises
------
    FileNotFoundError
        If the file doesnt exists

<a id="base_controller.BaseController.get_update_query"></a>

#### get\_update\_query

```python
@classmethod
def get_update_query(cls, file_name: str) -> str
```

Get one query on db/queries/update

Parameters
----------
file_name : str
    Name of the file inside the path without the file extension

Returns
-------
    A string with the query in the file 

Raises
------
    FileNotFoundError
        If the file doesnt exists

<a id="base_controller.BaseController.get_insert_query"></a>

#### get\_insert\_query

```python
@classmethod
def get_insert_query(cls, file_name: str) -> str
```

Get one query on db/queries/insert

Parameters
----------
file_name : str
    Name of the file inside the path without the file extension

Returns
-------
    A string with the query in the file

Raises
------
    FileNotFoundError
        If the file doesnt exists

<a id="coach_contracts_controller"></a>

# coach\_contracts\_controller

<a id="coach_contracts_controller.CoachContractsController"></a>

## CoachContractsController Objects

```python
class CoachContractsController(BaseController)
```

Class that manage the tournament.coach_contracts

...

Methods
-------
insert_coach_contracts(coach_contracts_data: list)
    Insert a list of tournament.coach_contracts in database

<a id="coach_contracts_controller.CoachContractsController.insert_coach_contracts"></a>

#### insert\_coach\_contracts

```python
@classmethod
def insert_coach_contracts(cls, coach_contracts_data: list) -> None
```

Insert a list of player_contracts_data into tournament.coach_contracts

Parameters
----------
coach_contracts_data : list
    A list of lists containing: 
    start: str, end: str, salary: int, club_id: int, coach_id: int

Returns
-------
    None

<a id="stadiums_controller"></a>

# stadiums\_controller

<a id="stadiums_controller.StadiumsController"></a>

## StadiumsController Objects

```python
class StadiumsController(BaseController)
```

Class that manage the tournament.stadiums

...

Methods
-------

select_all_stadiums()
    Select all stadiums from database

<a id="stadiums_controller.StadiumsController.select_all_stadiums"></a>

#### select\_all\_stadiums

```python
@classmethod
def select_all_stadiums(cls) -> list[set]
```

Select all stadiums from database

Returns
-------
    A list of lists with stadium data

<a id="players_controller"></a>

# players\_controller

<a id="players_controller.PlayersController"></a>

## PlayersController Objects

```python
class PlayersController(BaseController)
```

Class that manage the tournament.players

...

Methods
-------
insert_players(players_data: list)
    Insert a list of tournament.players in database
select_last_players()
    Select the 30 last tournament.players inserted
select_all_players_id()
    Select all the player's id of tournament.players
select_players_by_club(club_name: str, season: str)
    Select all players with contract with a specific club
select_players_with_contract(season: str)
    Select all players with contract with a club

<a id="players_controller.PlayersController.insert_players"></a>

#### insert\_players

```python
@classmethod
def insert_players(cls, players_data: list) -> None
```

Insert a list of players_data into tournament.players

Parameters
----------
players_data : list
    A list of lists containing: name: str, nationality: str, position: str, birth: int, height: float, weight: float, foot: str

Returns
-------
    None

<a id="players_controller.PlayersController.select_last_players"></a>

#### select\_last\_players

```python
@classmethod
def select_last_players(cls) -> list
```

Select the last players from tournament.players

Returns
-------
    A list with 30 length containing player information

<a id="players_controller.PlayersController.select_all_players_id"></a>

#### select\_all\_players\_id

```python
@classmethod
def select_all_players_id(cls) -> list
```

Select the player's id from tournament.players

Returns
-------
    A list with the id column from the tournament.players

<a id="players_controller.PlayersController.select_players_by_club"></a>

#### select\_players\_by\_club

```python
@classmethod
def select_players_by_club(cls, club_name: str, season: str) -> list[set]
```

Select players with contract of a club

Parameters
----------

club_name : str
    Club's name that will be used as parameter to the players
season : str
    Season that will be used as parameter to player_contracts extension

Returns
-------
    A list of Players data

<a id="players_controller.PlayersController.select_players_with_contract"></a>

#### select\_players\_with\_contract

```python
@classmethod
def select_players_with_contract(cls, season: str) -> list[set]
```

Select all players that have a contract with a club

Parameters
----------

season : str
    Season that will be used as parameter to player_contracts extension

Returns
-------
    A list of Players data

<a id="championship_controller"></a>

# championship\_controller

<a id="championship_controller.ChampionshipsController"></a>

## ChampionshipsController Objects

```python
class ChampionshipsController(BaseController)
```

Class that manage the tournament.championships table

...

Methods
-------

select_championships_table_by_club(season: int, club_id: int)
    Select one championships row by club
select_championship_table_by_division(season: int, division_name: str)
    Select all divisions championships rows by division & season
update_championship_table(data: list)
    Update a championships row

<a id="championship_controller.ChampionshipsController.select_championship_table_by_club"></a>

#### select\_championship\_table\_by\_club

```python
@classmethod
def select_championship_table_by_club(cls, season: int,
                                      club_id: int) -> list[set]
```

Select the club's championships table by his id

Parameters
----------
season : int
    To select the season of the championships
club_id : int
    To select the id from the club's championships

Returns
-------
    A list containing 
    matches, win, draw, loss, goals_for, goals_away, goals_conceded, goals_diff, points

<a id="championship_controller.ChampionshipsController.select_championship_table_by_division"></a>

#### select\_championship\_table\_by\_division

```python
@classmethod
def select_championship_table_by_division(cls, season: int,
                                          division_name: str) -> list[set]
```

Select all the rows of the championsips table based on the season and divison

Parameters
----------
season : int
    To select the season of the championships
division_name : str
    To select the championships division

Returns
-------
    A list of lists containing 
    matches, win, draw, loss, goals_for, goals_away, goals_diff, points

<a id="championship_controller.ChampionshipsController.update_championship_table"></a>

#### update\_championship\_table

```python
@classmethod
def update_championship_table(cls, data: list) -> None
```

Update the club's championships table based on division

Parameters
----------
data : list
    A list containing: points, win, loss, draw, goals_for, goals_away, goal_diff, club_id, season

Returns
-------
    None

<a id="overall_controller"></a>

# overall\_controller

<a id="overall_controller.OverallController"></a>

## OverallController Objects

```python
class OverallController(BaseController)
```

Class that manage the tournament.overall

...

Methods
-------
insert_overall(overall_data: list)
    Insert a list of tournament.overall in database

<a id="overall_controller.OverallController.insert_overall"></a>

#### insert\_overall

```python
@classmethod
def insert_overall(cls, overall_data: list) -> None
```

Insert a list of overall data into tournament.overall

Parameters
----------
overall_data : list
    A list of list containing
    season: str, overall: int, player_id: int

Returns
-------
    None

<a id="player_contracts_controller"></a>

# player\_contracts\_controller

<a id="player_contracts_controller.PlayerContractsController"></a>

## PlayerContractsController Objects

```python
class PlayerContractsController(BaseController)
```

Class that manage the tournament.player_contracts

...

Methods
-------
insert_player_contracts(player_contracts_data: list)
    Insert a list of tournament.player_contracts in database

<a id="player_contracts_controller.PlayerContractsController.insert_player_contracts"></a>

#### insert\_player\_contracts

```python
@classmethod
def insert_player_contracts(cls, player_contracts_data: list) -> None
```

Insert a list of player_contracts_data into tournament.player_contracts

Parameters
----------
player_contracts_data : list
    A list of lists containing: 
    start: str, end: str, salary: int, club_id: int, player_id: int

Returns
-------
    None

<a id="clubs_controller"></a>

# clubs\_controller

<a id="clubs_controller.ClubsController"></a>

## ClubsController Objects

```python
class ClubsController(BaseController)
```

Class that manage the tournament.clubs table

...

Methods
-------
select_id_name()
    Select all club's id and name
select_id()
    Select all club's id
select_serie_a_clubs()
    Select all clubs by serie a
select_serie_b_clubs()
    Select all clubs by serie b
select_serie_c_clubs()
    Select all clubs by serie c

<a id="clubs_controller.ClubsController.select_id_name"></a>

#### select\_id\_name

```python
@classmethod
def select_id_name(cls) -> list[set]
```

Select id and name from clubs

Returns
-------
    A list of lists with: id, name

<a id="clubs_controller.ClubsController.select_id"></a>

#### select\_id

```python
@classmethod
def select_id(cls) -> list[set]
```

Select id from clubs

Returns
-------
    A list of lists with: id

<a id="clubs_controller.ClubsController.select_serie_a_clubs"></a>

#### select\_serie\_a\_clubs

```python
@classmethod
def select_serie_a_clubs(cls) -> list[set]
```

Select all clubs that belongs to Serie A division

Returns
-------
    A list of lists with: id, name, country, division

<a id="clubs_controller.ClubsController.select_serie_b_clubs"></a>

#### select\_serie\_b\_clubs

```python
@classmethod
def select_serie_b_clubs(cls) -> list[set]
```

Select all clubs that belongs to Serie B division

Returns
-------
    A list of lists with: id, name, country, division

<a id="clubs_controller.ClubsController.select_serie_c_clubs"></a>

#### select\_serie\_c\_clubs

```python
@classmethod
def select_serie_c_clubs(cls) -> list[set]
```

Select all clubs that belongs to Serie C division

Returns
-------
    A list of lists with: id, name, country, division

<a id="games_controller"></a>

# games\_controller

<a id="games_controller.GamesController"></a>

## GamesController Objects

```python
class GamesController(BaseController)
```

Class that manage the tournament.games & game_stats table

...

Methods
-------

insert_games_list(games_data: list)
    Insert a list of tournament.games in database
insert_game_stat_with_id_return(game_data)
    Insert a tournament.game_stats in database
select_last_id()
    Select the last tournament.game_stats inserted

<a id="games_controller.GamesController.insert_games_list"></a>

#### insert\_games\_list

```python
@classmethod
def insert_games_list(cls, games_data: list) -> None
```

Insert a list of games_data into tournament.games

Parameters
----------

games_data : list
    A list of lists with games_data

Returns
-------
    None

<a id="games_controller.GamesController.insert_game_stat_with_id_return"></a>

#### insert\_game\_stat\_with\_id\_return

```python
@classmethod
def insert_game_stat_with_id_return(cls, game_data: list) -> list
```

Insert a list of games_data into tournament.game_stats

Parameters
----------

games_data : list
    A list with game_stats data

Returns
-------
    A list containing the game_stats.id from the game_stats inserted in db

<a id="games_controller.GamesController.select_last_id"></a>

#### select\_last\_id

```python
@classmethod
def select_last_id(cls) -> list
```

Select the last id from tournament.game_stats

Returns
-------
    A list with id from last game_stats row

<a id="coaches_controller"></a>

# coaches\_controller

<a id="coaches_controller.CoachesController"></a>

## CoachesController Objects

```python
class CoachesController(BaseController)
```

Class that manage the tournament.coaches

...

Methods
-------
insert_coaches(coaches_data: list)
    Insert a list of tournament.coaches in database
select_id()
    Select all coach's id

<a id="coaches_controller.CoachesController.insert_coaches"></a>

#### insert\_coaches

```python
@classmethod
def insert_coaches(cls, coaches_data: list) -> None
```

Insert a list of coaches_data into tournament.coaches

Parameters
----------
coaches_data : list
    A list of lists containing: 
    name: str, nationality: str, birth: int

Returns
-------
    None

<a id="coaches_controller.CoachesController.select_id"></a>

#### select\_id

```python
@classmethod
def select_id(cls) -> list[set]
```

Select id from coaches

Returns
-------
    A list of lists with: id

