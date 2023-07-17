<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Game</h3>

  <p align="center">
    	Defines a game class, handle the game execution and data export
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#game">Game</a></li>
	</ol>
</details>


## Game
#### Game(home_club, away_club, competition, m_round, season, head_stadium=None, verbose=False)

Methods defined here
```py
__init__(self, home_club, away_club, competition, m_round, season, head_stadium=None, verbose=False)
	Initialize self.  See help(type(self)) for accurate signature.

__repr__(self)
	Return repr(self).

__str__(self)
	Return str(self).

actions(self)
	Simulates a football actions, pass, defense, tackle and goals

add_assist(self, player)
	Add one assist to player

add_goal(self, player)
	Add one goal to player

add_matches(self, players)
	Add one match to player

add_points(self, players, points)
	Add points to player

add_stats(self, club, move)

check_game_stats(self)
	Check for clean sheets, hat tricks and update pontuation

check_subs(self, n_subs)
	Boolean: returns True if the team still have subs left

data(self)

decision(self, p_overall)

defense(self, keeper)
	Represents a defense, will add points to goalkeeper

finish(self, keeper, defensor, midfielder, attacker, club_finish)
	Represent a gols, will add points to attacker and remove opposite 
	and register the goals and asssits inside the class

get_score_board(self, end_game=False)
	move(self, attack_club, defense_club, field_part, sender=None)
	{
    	'destiny': ''
    	'club_possession': ''
    	'other_club': ''
    	'sender': ''
    
	}

penalty(self, keeper, attacker, club_finish)
	Represents a penalty kick

register_winner(self)
	Following the database needs, will return a dict
	{
    	home_team: [ won, draw, lost, goal_f, goal_a, goal_diff, points, club_name ],
    	away_team: [ ... ]
	}

select_player(self, club, player_position)
	Return a player from the club start eleven

set_options(self, player_position, bench)
	Return a list of players for a position that matches the player_position

start(self)
	Simultes a match

sub_points(self, player, points)
	Remove points to player

subs(self, club)
	Will make a sub if everything goes well return True

update_players_match_stats(self)
```

