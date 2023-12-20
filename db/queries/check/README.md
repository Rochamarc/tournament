# Checking queries
### Only for checking things before an insertion or update that can generate a bug
---
### Check Championships initial table
```sql
    SELECT id 
    FROM championships
    WHERE   club_id = %s
            AND season = %s;

    /* example */
    /* 
    each club in initial table has only one insertion by season 
    each club only plays one national tournament by season
    */
    
    SELECT id 
    FROM championships c 
    WHERE   club_id = 1 
            AND season = '2025';
```

### Check Championships
---
```sql
    /* This only apply to tournaments with 38 rounds, 20 clubs, (all x all) * 2 */

    SELECT championships.id 
    FROM championships
    INNER JOIN divisions
        ON championships.division_id = divisions.id
    INNER JOIN competitions 
        ON divisions.competition_id = competitions.id
    WHERE   (championships.club_id = %s
            AND championships.season = %s  
            AND competitions.name = %s 
            AND championships.matches < 38);


    /* example 
    if i make a mistake on the main file, and put the wrong season, a previous one for example
    this will return nothing and python will handle the error
    */

    SELECT championships.id 
    FROM championships
    INNER JOIN divisions
        ON championships.division_id = divisions.id
    INNER JOIN competitions 
        ON divisions.competition_id = competitions.id
    WHERE   (championships.club_id = 1
            AND championships.season = '2022' 
            AND competitions.name = 'Campeonato Brasileiro'
            AND championships.matches < 38);
    
```
---
### Check Champions
---
```sql
    SELECT  champions.id
    FROM champions
    INNER JOIN divisions
        ON champions.division_id = divisions.id 
    INNER JOIN competitions
        ON divisions.competition_id = competitions.id
    WHERE   (competitions.name = 'Campeonato Brasileiro' 
            AND divisions.name = 'Serie A' 
            AND champions.season = '2022');
    
```
