<br />
<!-- The header -->
<div align="center">
  <h3 align="center">Classes</h3>

  <p align="center">
    Base classes for the tournament
    <br />
</div>

<!-- builting -->
<details>
	<summary>builting.objects</summary>
	<ol>
		<li><a href="#club">Club</a></li>
		<li><a href="#player">Player</a></li>
		<li><a href="#stadium">Stadium</a></li>
	</ol>
</details>


## Club
#### Club(name, country, club_class, state=None, save_file=None)
	
Methods defined here
```py
__init__(self, name, country, club_class, state=None, save_file=None)
	Initialize self.  See help(type(self)) for accurate signature.

__repr__(self)
	Return repr(self).

generate_coeff(self)

set_coeff(self)

set_formation(self, players_list)
	Receive a list of players 

	id | name | nationality | age | overall | club | position | matches_played | goals | assists | points | avg | save_file
```

Readonly properties defined here
```py
data
	Return a list with name, country, state, coeff, club_class

overall
	Define the club overall on the average of player overall
```

## Player
#### Player(name, nationality, age, position, min_coeff, max_coeff, current_club=None, shirt_number=None, save_file=None)

Methods defined here:
```py
__init__(self, name, nationality, age, position, min_coeff, max_coeff, current_club=None, shirt_number=None, save_file=None)
	Initialize self.  See help(type(self)) for accurate signature.

__repr__(self)
	Return repr(self).

__str__(self)
	Return str(self).

get_competition_stats(self)
	return matches_played, goals, assists, points
``` 

Readonly properties defined here:
```py
avg

data
	return list[name, nationality, age, overall, current_club, position, matches, goals, assists, avg]
```

## Stadium
#### Stadium(name, location, capacity=None, club_owner=None)
 
Methods defined here:
```py
__init__(self, name, location, capacity=None, club_owner=None)
	Initialize self.  See help(type(self)) for accurate signature.

__repr__(self)
	Return repr(self).

get_info(self)
```

Readonly properties defined here:
```py
data
```