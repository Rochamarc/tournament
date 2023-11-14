# Database Docs

<p>Database name: <b>tournament</b></p>

## Tables
### Clubs
---
```sql
    id PRIMARY KEY
    name VARCHAR(100)
    country VARCHAR(100)
```

### Coaches
---
```sql
    id PRIMARY KEY
    name VARCHAR(100)
    nationality VARCHAR(100)
    birth CHAR(4)
```

### Players
---
```sql
    id PRIMARY KEY
    name VARCHAR(100)
    nationality VARCHAR(100)
    position CHAR(2)
    birth CHAR(4)
    height FLOAT
    weight FLOAT
    foot CHAR(1)
```

### Stadiums
---
```sql
    id PRIMARY KEY
    name VARHCAR(100)
    country VARCHAR(100)
    city VARCHAR(100)
    capacity INT
```

### Players Contract
---
```sql
    id PRIMARY KEY
    start CHAR(4)
    end CHAR(4)
    transfer_amount INT
    salary INT
    termination_fine INT 
    club_id FOREIGN KEY
    player_id FOREIGN KEY
```

### Coaches Contract
---
```sql
    id PRIMARY KEY
    start CHAR(4)
    end CHAR(4)
    salary INT
    termination_fine INT 
    club_id FOREIGN KEY
    coach_id FOREIGN KEY
```

### Stats
---
```sql
    id PRIMARY KEY
    season CHAR(4)
    matches INT
    goals INT
    assists INT
    tackles INT
    passes INT
    wrong_passes INT
    intercepted_passes INT 
    clearences INT
    stolen_balls INT
    clean_sheets INT
    defenses INT
    difficult_defenses INT
    goals_conceded INT
    player_id FOREIGN KEY
```

### Market Value
---
```sql
    id PRIMARY KEY
    season CHAR(4)
    value INT
    player_id FOREIGN KEY 
```

### Skills
---
```sql
    id PRIMARY KEY
    season CHAR(4)
    positioning INT
	reflexes INT
	diving INT
	standing_tackle INT
	physical INT
	passing INT
    dribbling INT
	long_shot INT
	finishing INT
	player_id FOREIGN KEY
```

### Retired Players
---
```sql
    id PRIMARY KEY
    id_player INT
    name VARCHAR(100)
    nationality VARCHAR(100)
    position CHAR(2)
    birth CHAR(4)
    foot CHAR(1)
```

### Games
---
```sql
    id PRIMARY KEY
    season CHAR(4)
    hour CHAR(5)
    climate VARCHAR(5)
    weather VARCHAR(10)
    stadium VARCHAR(100)
    audience INT
    ticket_value INT
    home_game_stats_id FOREIGN KEY
    away_game_stats_id FOREIGN KEY
```


### Game Stats
---
```sql
    id PRIMARY KEY
    goals INT
    shots INT
    shots_on_target INT
    fouls INT
    passes INT
    wrong_passes INT
    interceptations INT
    tackles INT
    stolen_balls INT
    saves INT
    ball_possession INT
    offsides INT
    freekicks INT
    penalties INT
    club_id FOREIGN KEY
```

### Player Game Stats
---
```sql
	id PRIMARY KEY
	assists INT
	goals INT
	tackles INT
	defenses INT
	passes INT
	wrong_passes INT
	intercepted_passes INT
	dificult_defenses INT
	clearances INT
	fouls INT
	stolen_balls INT
	player_id FOREIGN KEY
	game_id FOREIGN KEY
```

### Championships
---
```sql
    id PRIMARY KEY
    season CHAR(4)
    division VARCHAR(30)
    matches INT 
    win INT
    loss INT
    draw INT
    goals_for INT
    goals_away INT
    goals_diff INT
    points INT
    club_id FOREIGN KEY
```

### Competitions
```sql
    id PRIMARY KEY
    name VARCHAR(100)
```

### Divions
```sql
    id PRIMARY KEY
    name VARCHAR(100)
    competition_id FOREIGN KEY
```

### Stadium_Ownership
```sql
    id PRIMARY KEY
    club_id INT
    stadium_id FOREIGN KEY
```

### Back to the main file
([Go Back](../README.md)) 