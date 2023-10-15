# Name Generator

## This module handles the naming of players and coaches

### Initialize
---
* Copy the content on main.sql and paste on mysql or run 
  ```sh
   ./database_initialize.sh
   ```
* The run the two notebooks to insert the data into the database


### Content tables
---
> Sql table description

### first_names
```sql
id INT PRIMARY KEY,
value VARCHAR(100),
nationality VARCHAR(100)
```

### last_names
```sql
id INT PRIMARY KEY,
value VARCHAR(100),
nationality VARCHAR(100)
```

### Content files
---
### First Names
> List of names in the first names table

*   Asian
    *   Korean
    *   Chinese
    *   Japanese
*   Brazilian
*   European
*   North American
    *   English
    *   Spanish
*   South American
    *   Portuguese
    *   Spanish

### Last Names
> List of names in the last names table

*   Asian
*   English
*   European
*   Hispanic
*   South American
    *   Portuguese
    *   Spanish
*   Spanish