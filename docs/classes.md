# Table of Contents

* [coach](#coach)
  * [Coach](#coach.Coach)
* [player](#player)
  * [Player](#player.Player)
* [club](#club)
  * [Club](#club.Club)
* [person](#person)
* [stadium](#stadium)
  * [Stadium](#stadium.Stadium)
* [formation](#formation)
  * [Formation](#formation.Formation)
    * [starting\_eleven](#formation.Formation.starting_eleven)
    * [backups](#formation.Formation.backups)
    * [select\_keepers](#formation.Formation.select_keepers)
    * [select\_backs](#formation.Formation.select_backs)
    * [select\_mids](#formation.Formation.select_mids)
    * [select\_fronts](#formation.Formation.select_fronts)
    * [sorted\_by\_overall](#formation.Formation.sorted_by_overall)

<a id="coach"></a>

# coach

<a id="coach.Coach"></a>

## Coach Objects

```python
class Coach(Person)
```

A class that represents a Football/Soccer Coach

...

Attributes
----------
    id :  int
        Unique value the representes each coach
    name : str
        The name of the coach
    nationality : str
        The nationality from the coach
    birth : int
        The birth year of the coach

<a id="player"></a>

# player

<a id="player.Player"></a>

## Player Objects

```python
class Player(Person)
```

A class that represents a Football/Soccer player

...

Attributes
----------
    id :  int
        Unique value the representes each coach
    name : str
        The name of the coach
    nationality : str
        The nationality from the coach
    birth : int
        The birth year of the coach
    position : str
        Two capital letters that represents the players position
    height : float
        Players height
    weight : float
        Players weight
    foot : str
        A capital letter that represents the player favorite foot
    overall : int
        A value from 56 to 100 that represents how good the player is
    club_id : int
        The id from the club that the athlete plays for

<a id="club"></a>

# club

<a id="club.Club"></a>

## Club Objects

```python
class Club()
```

A class that represents a Football/Soccer Club

...

Attributes
----------
    id :  int
        Unique value the representes each club
    name : str
        The name of the club
    country : str
        The nationality from the club
    short_country : str
        The three initials letters from the club's country
    squad : list
        A list of every athlete that plays for the club
    start_eleven : list
        A list of the 11 players that start the matches
    bench : list
        A list of the remaining players

Methods
-------
    add_to_squad(values: list)
        Add players to the squad
    add_to_start_eleven(values: list)
        Add players to start_eleven
    add_to_bench(values: list)
        Add players to bench

<a id="person"></a>

# person

<a id="stadium"></a>

# stadium

<a id="stadium.Stadium"></a>

## Stadium Objects

```python
class Stadium()
```

A class that represents a Football/Soccer Stadium

...

Attributes
----------
    name : str
        The name of the Stadium
    location : str
        The location of the stadium
    capacity : int
        The maximum capacity of audience supported by the stadium

<a id="formation"></a>

# formation

<a id="formation.Formation"></a>

## Formation Objects

```python
class Formation()
```

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

<a id="formation.Formation.starting_eleven"></a>

#### starting\_eleven

```python
@classmethod
def starting_eleven(cls, squad: list) -> list
```

Add players to a list based on player's overall

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

<a id="formation.Formation.backups"></a>

#### backups

```python
@staticmethod
def backups(squad: list, starting_eleven: list) -> list
```

Add players to a list based on the players that are not in starting_eleven

Parameters
----------
squad : list
    A list of Player Objects
starting_eleven : list
    A list with eleven Player Objects

Returns
-------
    A list that match de difference between squad and starting_eleven

<a id="formation.Formation.select_keepers"></a>

#### select\_keepers

```python
@classmethod
def select_keepers(cls, squad: list) -> list
```

Select goalkeepers

Parameters
----------
squad : list
    A list of Player Object

Returns
-------
    A list of players that have Player.position = 'GK'

<a id="formation.Formation.select_backs"></a>

#### select\_backs

```python
@classmethod
def select_backs(cls, squad: list) -> list
```

Select defensive players

Parameters
----------
squad : list
    A list of Player Object

Returns
-------
    A list of players that have Player.position = CB, RB or LB

<a id="formation.Formation.select_mids"></a>

#### select\_mids

```python
@classmethod
def select_mids(cls, squad: list) -> list
```

Select midifielder players

Parameters
----------
squad : list
    A list of Player Object

Returns
-------
    A list of players that have Player.position = DM, CM, AM, LM or RM

<a id="formation.Formation.select_fronts"></a>

#### select\_fronts

```python
@classmethod
def select_fronts(cls, squad: list) -> list
```

Select attacking players

Parameters
----------
squad : list
    A list of Player Object

Returns
-------
    A list of players that have Player.position = CF, SS or WG

<a id="formation.Formation.sorted_by_overall"></a>

#### sorted\_by\_overall

```python
@classmethod
def sorted_by_overall(cls, players: list, reverse=False) -> list
```

Sort the players based on Player.overall

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

