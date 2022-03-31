<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Ranking</h3>

  <p align="center">
    	Handle tables with dataframes. Will create the league tables.
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#ranking">Ranking</a></li>
	</ol>
</details>

## Modules

1. csv
2. pandas
3. sqlite3


## Ranking

Static methods defined here
```py
define_conmebol_points(clubs)
	Define the commebol ranking based on the csv file

domestic_table(division, season)
	Return a panda series with the tables below
	Position    Club    Matches    Won  Draw    Lost   Goals For    Goals Away    Goals Diff    Points

individual_leaderboard(all_clubs, category, season, save_file=None)
	Return a dataframe contains name, current_club, position, matches_played, goals, assists, average

international_group_table(season)
	Return a panda series with the group stage tables

player_info(players)
	Return a squad dataframe from the players inside the club
```

