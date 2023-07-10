from db.player_controller import PlayerData
from classes_helper import GenerateClass
from knock_out import KnockOutGame
from random import choice 

player_data = PlayerData()
generate = GenerateClass()

class Cup:
    def __init__(self, competition_name, season, phase, matches):
        self.competition_name = competition_name
        self.season = season
        self.phase = phase 

        self.matches = matches

        self.stadiums = generate.reconstruct_stadiums() 
    
    def run(self):
        results = []

        for match in self.matches:
            match[0].set_formation(player_data.get_players(match[0].name))
            match[1].set_formation(player_data.get_players(match[1].name))
            m_1 = KnockOutGame(match[0], match[1], 'Copa do Brasil', 1, self.season, 'First Phase', head_stadium=choice(self.stadiums), verbose=False).first_leg()
            results.append(m_1)
        
        return [ i['winner'] for i in results ]

    def show(self):
        print(f"{self.competition_name.upper()}")
        print(f"{self.season}")
        print(f"{self.phase}\n")
        for i in self.matches:
            print("="*50)
            print(f"{i[0]} x {i[1]}")
            print("="*50)
