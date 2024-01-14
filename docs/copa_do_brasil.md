# Copa do Brasil Database Schema

### Data Model
```
    First insertions:
        game_stats  -> home_game_stats
                    -> away_game_stats
    Second insertion:
        game -> home_game_stats_id & away_game_stats_id
    Third insertion:
        knock_out -> game_id

```

### Insertion mode
---
* Insert the game_stats and receives the two id's
* Insert the game with the game_stats.id's and receive the game.id
* insert the knock_out with the game.id and penalties.id if true