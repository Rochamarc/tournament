# Classes Docs

#### Club

* Generating a new club
    ```py
    Club('name':str,'country':str,'club_class':str, state=None)
    ```

#### Player

* Generating a new player
    ```py
    Player('id':int, 'name':str, 'nationality':str, 'birth':int, 'position':str, 'height': float, 'weight':float, 'foot':str, 'overall':int, 'club_id': int)
    ```

#### Stadium

* Generating a new stadium
    ```py
    Stadium('name':str, 'location':str, 'capacity'=None, 'club_owner'=None)
    ```

# Mudanças

` O ideal é que as classes parem de gerar ou criar coisas, eles sirvam somente para 'storar' dados que venham do banco. Algumas funções e métodos que devem ir embora`

### Player
---

* Player.overall
* Player.set_height
* Player.weight -> Nesse caso o self.weight ja gera um peso
* Player.market_value
* Player.salary
* Entre outras funções que alteram a estrutura da nossa classe


No caso do _market_value_ e _salary_ talvez seja o caso até ir embora ou ficar como uma função com decorador property que chame isso quando for necessario, pois para o funcionamento da maior parte do codigo essa parte é completamente desnecessaria, pesando desnecessariamente a nossa classe.

### Coach
---

* Coach.technical_features


### Person
---

* Person.increase_age

### Club
---

`A mesma lógica aplicada em players será aplicada em clubs, funções e variaveis como total_budget, salary_budget, generate_coeff(), set_formation() todas vao possivelmente embora e terá novas funcionalidades que criem toda estrutura de uma só vez e gere uma serie de arquivos que sirvam de base apensar para serem abertos ou puchados da base de dados. `