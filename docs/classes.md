# Classes Docs

### Club

* Generating a new club
    ```py
    Club(id: int, name:str, country:str)
    ```
* methods
    ```py
    Club().add_to_squad(values: list)
    Club().add_to_start_eleven(values: list)
    Club().add_to_bench(values: list)
    ```

### Player

* Generating a new player
    ```py
    Player(id:int, name:str, nationality:str, birth:int, position:str, height: float, weight:float, foot:str, overall:int, club_id: int)
    ```

### Coach

* Generating a new player
    ```py
    Coach(id: int, name: str, nationality: str, birth: int)
    ```


### Stadium

* Generating a new stadium
    ```py
    Stadium(name:str, location:str, capacity=None)
    ```
