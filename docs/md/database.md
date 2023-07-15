<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Database</h3>

  <p align="center">
    Module that handles database classes and functions
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#clubdata">ClubData</a></li>
		<li><a href="#domesticleague">DomesticLeague</a></li>
		<li><a href="#gamedata">GameData</a></li>
				<li><a href="#internationalcup">InternationalCup</a></li>
		<li><a href="#playerdata">PlayerData</a></li>
		<li><a href="#stadiumdata">StadiumData</a></li>
	</ol>
</details>

# Classes

## ClubData
	
Static methods defined here:
```py
get_clubs(club_name, verbose=False)
	Get clubs info from database

insert_clubs_db(clubs, verbose=False)
	Insert clubs into the databse
```

## DomesticLeague

Static methods defined here
```py
create_domestic_table(division, season, verbose=False)

domestic_table_basic(club_names, division, season, verbose=False)
	Insert club domestic cup data into the database

get_domestic_cup_table(division, season)
	Get the domestic cup table data

update_domestic_table(club_stats, division, season)

``` 

## GameData 

Static methods defined here
```py
insert_games_db(game_list, verbose=False)
	Insert game data into database 
 
	below the order to receive the data 
	[ competition, season, hour, home_team, away_team, score, stadium, home_shots, home_shots_on_target, home_fouls, 
	home_tackles, home_saves, home_ball_possession, home_offsides, home_freekicks, away_shots, away_shots_on_target,
	away_fouls, away_tackles, away_saves, away_ball_possession, away_offsides, away_freekicks ]
```

## InternationalCup

Static methods defined here
```py
create_international_cup(season, group, verbose=False)
	Create international cup table

get_group_stage_data(season)
	Get international cup group stage 
	return dict { 'A' : [data], ... }

international_group_table_basic(club_names, season, group, verbose=False)
	Basic international cup data

update_international_table(club_stats, group, season)
	Insert into the international cup table
```

## PlayerData

Static methods defined here
```py
get_players(club_name, verbose=False)
	Get the players info from database

insert_players_db(players, verbose=False)
	Insert players data into the database

update_player_stats(player_list, verbose=False)
```

## StadiumData

Static methods defined here
```py
get_stadiums()
	Get stadiums data

insert_stadiums_db(stadiums, verbose=False)
	Insert stadiums to the database
```

# Functions

```py
create_db()
	Create database tables

upload_ranking_db(verbose=False)
	Upload conmebol ranking
```

# Data

```py
database = 'database.db'
```

