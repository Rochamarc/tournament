from random import choice, randint
import numpy as np
from pprint import pprint
import pandas as pd
import os
import sqlite3
from faker import Faker

fake = Faker()

class Club:

    def __init__(self,name,country):
        self.name = name
        self.country = country
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goals_balance = 0
        self.victory = 0
        self.draw = 0
        self.defeat = 0
        self.games_played = 0
        self.club_force = 0 # club overall

        # squad
        self.squad = {}
        self.formation = None
        self.start_eleven = []
        self.reserve = []
        self.unrelated = []

    def __repr__(self):
        return self.name

    def show_season_stats(self):
        print(f"""
        {self.name.upper()}

        Group Stage Points:
        {self.points}

        Victory:
        {self.victory}

        Draws:
        {self.draw}

        Defeat:
        {self.defeat}

        Goals Scored:
        {self.goals_scored}

        Goals Conceded:
        {self.goals_conceded}

        Goals Diff:
        {self.goals_balance}
        """)

    def register_squad(self):
        self.squad["goal_keeper"] = [ Player(fake.name_male(), fake.country(), randint(16,37), 'Goalkeeper', current_club=self.name ) for _ in range(3) ] # 3 goleiros
        self.squad["defender"] = [ Player(fake.name_male(), fake.country(), randint(16,37), choice(['Center Back', 'Left Back', 'Right Back']),  current_club=self.name ) for _ in range(12) ]
        self.squad["midfielder"] = [ Player(fake.name_male(), fake.country(), randint(16,37), choice(['Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder']),  current_club=self.name ) for _ in range(12) ]
        self.squad["attacker"] = [ Player(fake.name_male(), fake.country(), randint(16,37), choice(['Center Forward', 'Second Striker', 'Winger']), current_club=self.name ) for _ in range(6)  ]

        # registrate on the database
        print("Inserting players into database")
        for player in self.squad["goal_keeper"]:
            player.db_insertion()
        for player in self.squad['defender']:
            player.db_insertion()
        for player in self.squad['midfielder']:
            player.db_insertion()
        for player in self.squad['attacker']:
            player.db_insertion()
        print("Insertion completed sucessfully!")
        
    def show_cast(self):
        # return name, position, matches, goals, assists, average points
        players = []

        for player in self.start_eleven:
            players.append(player.return_stats())
        for player in self.reserve:
            players.append(player.return_stats())
        for player in self.unrelated:
            players.append(player.return_stats())

        return pd.DataFrame(players, index=None, columns=['Name','Position','MP','GS','A','Avg'])

    def show_formation(self):
        print(f"FORMATION: {self.formation}\n")

        print("STARTING ELEVEN\n")
        for player in self.start_eleven:
            player.basic_info()

        print("REVERSER\n")
        for player in self.reserve:
            player.basic_info()

        print("UNRELATAED\n")
        for player in self.unrelated:
            player.basic_info()

    def formation_auto(self):
        # sorting squad
        for key, value in self.squad.items():
            value.sort(key=lambda player: player.overall, reverse=True)

        cp_squad = self.squad.copy()

        self.formation = choice(['3-5-2', '4-3-3', '4-4-2'])

        self.start_eleven.append(cp_squad['goal_keeper'][0])
        del cp_squad['goal_keeper'][0]

        self.reserve.append(cp_squad['goal_keeper'][1])
        del cp_squad['goal_keeper'][0]

        # garbage code
        if self.formation == '3-5-2':
            for i in range(3):
                self.start_eleven.append(cp_squad['defender'][0])
                del cp_squad['defender'][0]
            for i in range(5):
                self.start_eleven.append(cp_squad['midfielder'][0])
                del cp_squad['midfielder'][0]
            for i in range(2):
                self.start_eleven.append(cp_squad['attacker'][0])
                del cp_squad['attacker'][0]
        if self.formation == '4-3-3':
            for i in range(4):
                self.start_eleven.append(cp_squad['defender'][0])
                del cp_squad['defender'][0]
            for i in range(3):
                self.start_eleven.append(cp_squad['midfielder'][0])
                del cp_squad['midfielder'][0]
            for i in range(3):
                self.start_eleven.append(cp_squad['attacker'][0])
                del cp_squad['attacker'][0]
        if self.formation == '4-4-2':
            for i in range(4):
                self.start_eleven.append(cp_squad['defender'][0])
                del cp_squad['defender'][0]
            for i in range(4):
                self.start_eleven.append(cp_squad['midfielder'][0])
                del cp_squad['midfielder'][0]
            for i in range(2):
                self.start_eleven.append(cp_squad['attacker'][0])
                del cp_squad['attacker'][0]

        for i in range(2):
            self.reserve.append(cp_squad['defender'][0])
            self.reserve.append(cp_squad['midfielder'][0])
            self.reserve.append(cp_squad['attacker'][0])

            del cp_squad['defender'][0]
            del cp_squad['midfielder'][0]
            del cp_squad['attacker'][0]

        for position, players in cp_squad.items():
            for player in players:
                self.unrelated.append(player)

        self.squad = {}

    def register_game(self, goals_scored, goals_conceded):
        if goals_scored > goals_conceded:
            self.points += 3
            self.victory += 1
        if goals_scored == goals_conceded:
            self.points += 1
            self.draw += 1
        if goals_scored < goals_conceded:
            self.defeat += 1

        self.balance_goals(goals_scored, goals_conceded)

    def register_knock_out_game(self, goals_scored, goals_conceded):
        if goals_scored > goals_conceded:
            self.victory += 1
        if goals_scored == goals_conceded:
            self.draw += 1
        if goals_scored < goals_conceded:
            self.defeat += 1

        self.balance_goals(goals_scored, goals_conceded)


    # Balanceando os gols
    def balance_goals(self,goals_scored,goals_conceded):
        self.games_played += 1
        self.goals_scored += goals_scored
        self.goals_conceded += goals_conceded
        self.goals_balance += goals_scored - goals_conceded

    def show_stats(self):
        return [self.name, self.points, self.victory, self.draw, self.defeat, self.goals_scored, self.goals_conceded, self.goals_balance]

#### Player Base Object #####
class Player:

    def __init__(self, name, nationality, age, position, current_club=None):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.overall = randint(65,89)
        self.current_club = current_club
        self.position = position

        #stats de competição
        self.matches_played = 0
        self.goals = 0
        self.assists = 0
        self.points = [] # every match another point is add here, thent is calculated by the average
        self.avg = self.average()

    def average(self):
        try:
            return len(self.points) / sum(self.points)
        except:
            return 0

    # Gera o output pro desenvolvedor
    def __repr__(self):
        return self.name

    # Gera o output para o usuario final
    def __str__(self):
        return self.name

    def basic_info(self):
        print(f"{self.name} :: {self.overall} \n{self.position}\n")

    def show(self):
        print(f"""
        Name: {self.name}
        Overall: {self.overall}
        Position: {self.position}
        Current Club: {self.current_club}
        Age: {self.age}
        Nationality: {self.nationality}
        """)

    def return_stats(self):
        # return name, position, matches, goals, assists, average points
        return [self.name,  self.position, self.matches_played, self.goals, self.assists, self.avg ]

    def return_personal_stats(self):
        # return name, position, overall, age
        return [self.name, self.nationality, self.current_club, self.age, self.position, self.overall]

    def db_insertion(self):
        ls = [ self.name, self.nationality, self.age, self.overall, self.current_club, self.position, self.matches_played, self.goals, self.assists, self.avg ]

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO player (name, nationality, age, overall, current_club, position, matches_played, goals, assists, avg) VALUES (?,?,?,?,?,?,?,?,?,?)", ls)

        conn.commit() # save the changes
        conn.close()

class Stadium:

    def __init__(self, name, location, capacity=None, club_owner=None):
        self.name = name 
        self.location = location # City, Country ex: Manchester, UK
        self.club_owner = club_owner 
        if not capacity:
            self.capacity = randint(10_000, 50_000)
        else:
            self.capacity = capacity

    def show_info(self):
        print(f"NAME: {self.name}")
        print(f"LOCATION: {self.location}")
        print(f"CAPACITY: {self.capacity}")
        print(f"OWNER: {self.club_owner}")

    def db_insertion(self):

        ls = [ self.name, self.location, self.club_owner, self.capacity ]

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO stadium (name, location, club_owner, capacity) VALUES (?,?,?,?)", ls)

        conn.commit()
        conn.close()