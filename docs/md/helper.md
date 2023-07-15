<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Helper</h3>

  <p align="center">
    Secundary classes
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#generate-class">Helper</a></li>
	</ol>
</details>


## Helper

Static methods
```py
def define_clubs_stadium(clubs: list, stadiums: list) ‑> None

    Defines a stadium to a club if the have a stadium Defines a generic stadium to a club if he dosent have one
```

```py
def get_clubs_by_file(text_file_path: str) ‑> list

    Get clubs by file and return a list of clubs

``` 
```py
def get_players_list(clubs: list) ‑> list

    Return a list with all players
```     
```py
def loop_for_clubs(club_data: list) ‑> list

    Loop through the club_data and return a list
```     
```py
def reconstruct_club_by_line(line: str) ‑> classes.club.Club

    Return a list of clubs, created by a line of data
```     
```py
def reconstruct_clubs(division: str, season: str) ‑> list

    Return the list of the clubs
```     
```py
def reconstruct_international_clubs(country: str) ‑> list

    Return the list of the clubs
```     
```py
def reconstruct_stadiums() ‑> list

    Return list of stadiums
```     
```py
def set_clubs(text_file_path: str) ‑> list

    Return a list of Clubs
```     
```py
def set_defenders(club: classes.club.Club, country: str, min_club_coeff: int, max_club_coeff: int, length=12) ‑> list

    Return a list of 12 defenders, CB, LB and RB
```     
```py
def set_forwards(club: classes.club.Club, country: str, min_club_coeff: int, max_club_coeff: int, length=6) ‑> list

    Return a list of 6 forwards, CF, SS and WG
```     
```py
def set_generic_stadium(club_country: str) ‑> classes.stadium.Stadium

    Set a generic stadium
```     
```py
def set_keepers(club: classes.club.Club, country: str, min_club_coeff: int, max_club_coeff: int, length=3) ‑> list

    Return a list of keepers
```     
```py
def set_midfielders(club: classes.club.Club, country: str, min_club_coeff: int, max_club_coeff: int, length=12) ‑> list

    Return a list of 12 midfielders, DM, CM and AM
```     
```py
def set_players(club: classes.club.Club, country: str, min_club_coeff: int, max_club_coeff: int) ‑> list

    Return a list of players designated to the club
```     
```py
def set_stadium() ‑> list
```     
```py
def update_player_stats(clubs: list) ‑> None

    Update players stats return None
```