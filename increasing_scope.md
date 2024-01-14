# Market

## Queries
```
    update_player_contracts -> query
```

## Controllers
```
    find_players_with_no_contract() -> controller
    find_players_with_end_contract(season) -> controller
    find_good_players(overall_range) -> controller
    find_cheap_players(termination_fine or market_value) -> controller
    end_contract_with_clubs(season) -> controller
```

* puxar todos os jogadores no main, com ou sem contrato
* salvar esses jogadres numa lista distinda e deixa-los disponiveis para compra e venda
* todo inicio de temporada para gerar 

# TODO
* add gloves to player_contracts (this is what clubs are gona pay for the players with no contract, probably gonna add a glove as 10 or 20 per cent of the market_value)
* this controllers has to get the market value also
* Add a new table with a trigger on update to mark the changes