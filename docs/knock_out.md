# Knock out schema

## knock_out.match_number = 1
```py
home = 'Fluminense'
away = 'Flamengo'

home_goals = 2
away_goals = 1
```

## knock_out.match_number = 2
```py
home = 'Flamengo'
away = 'Fluminense'

home_goals = 1
away_goals = 0

penalties = True
home_penalties = 4
away_penalties = 5

```

# Results
```cs
+------------+---------------+---------------+-----------+---------------+
|    club    |   home_goals  |   away_goals  |   Total   |   Penalties   |
+------------+---------------+---------------+-----------+---------------+ 
| Fluminense |       2       |       0       |     2     |       5       |
|------------------------------------------------------------------------|
|  Flamengo  |       1       |       1       |     2     |       4       |
+------------+---------------+---------------+-----------+---------------+
```

### Winner = Fluminense