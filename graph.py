import matplotlib.pyplot as plt
from database import DomesticLeague, PlayerData

domestic = DomesticLeague()
player = PlayerData()

clubs_data = domestic.get_domestic_cup_table('serie_a', '2021')
clubs_names = [ c[1] for c in clubs_data ]

overall = {}

for club in clubs_names:
    plr = player.get_players(club) # get the players
        
    overall[club] = [ p[4] for p in plr ]

print(overall)

# Clubs names
x = [ (sum(over)/ len(over)) for name, over in overall.items() ]

# Clubs overall 
y = clubs_names

plt.plot(x,y)

# Naming
plt.ylabel('Clubs Names')
plt.xlabel('Overall')

# Title
plt.title('Clubs stats')

plt.show()