from controllers.market_controller import MarketController

import pandas as pd 

market_controller = MarketController()

players = market_controller.search_by_all('CF', 80, 2022)

header = ['id', 'name', 'nationality', 'position', 'age', 'height', 'foot', 'overall', 'market_value', 'salary', 'current_club']

print(pd.DataFrame(players, columns=header))