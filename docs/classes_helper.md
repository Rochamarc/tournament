<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Classes Helper</h3>

  <p align="center">
    Secundary classes
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#generate-class">Generate Class</a></li>
	</ol>
</details>


## Generate Class

Static methods defined here
```py
define_clubs_stadium(clubs, stadiums)
	Defines a stadium to a club if the have a stadium 
	Defines a generic stadium to a club if he dosent have one

define_schedule(clubs, stadiums)
	Return a dict of lists with all the rounds filled with
	[ home_club, away_club, stadium ]

get_players_list(clubs)
	Return a list with all players data enrolled on the championship

promotions_and_relegations(season, verbose=False)
	Promove and relegates all the divisions of the domestic league
	return a dict with the promoted and relegated clubs

reconstruct_clubs(division, season)
	Return the list of the clubs

reconstruct_stadiums()
	Return list of stadiums

set_clubs(text_file_path)
	Generate a list of clubs <class 'Club'> 
	return a list(clubs)

set_generic_stadium(club_country)
	Set a generic stadium

set_players(club_name, country, min_club_coeff, max_club_coeff)
	Generate players <class 'Player'> to the club <class 'Club'> 
	return a dict

set_stadium()

update_player_stats(clubs)
	Update players stats return None
```

