from random import choice, randint
import numpy as np
from pprint import pprint
import pandas as pd
import os
import sqlite3
from faker import Faker
from name_nationality import *

fake = Faker()

class Club:

    def __init__(self,name,country,save_file=None):
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goals_balance = 0
        self.victory = 0
        self.draw = 0
        self.defeat = 0
        self.games_played = 0
        self.club_force = 0 # club overall
        self.ranking_points = 0
        self.coeff = self.coeff()
        self.save_file = save_file
        # squad
        self.squad = { 'goal_keeper': [], 'defender': [], 'midfielder': [], 'attacker': [] }
        self.formation = None
        self.start_eleven = []
        self.bench = []
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

    def coeff(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor() 

        cursor.execute("SELECT points FROM clubs_ranking WHERE name=?", (self.name,))

        val = cursor.fetchall()[0][0]
        
        v_coeff = 65

        if val >= 800:
            v_coeff += 1
        if val >= 900:
            v_coeff += 1
        if val >= 1000:
            v_coeff += 2
        if val >= 3000:
            v_coeff += 2
        if val >= 4000:
            v_coeff += 2
        if val >= 5000:
            v_coeff += 2
        if val >= 6000:
            v_coeff += 2
        else:
            v_coeff += 1

        return v_coeff
    def register_squad(self, skip_db=False):
        shirt_numbers = [ x for x in range(1,50) ]

        for _ in range(3):
            natio_ = generate_nationality(self.country)
            name_ = generate_name(natio_) 
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            self.squad['goal_keeper'].append(Player(name_, natio_, randint(16,37), 'Goalkeeper', current_club=self.name, shirt_number=number, club_coeff=self.coeff, save_file=self.save_file))
        for _ in range(12):
            natio_ = generate_nationality(self.country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Center Back', 'Left Back', 'Right Back'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            self.squad['defender'].append(Player(name_, natio_, randint(16,37), pos_,  current_club=self.name, shirt_number=number, club_coeff=self.coeff, save_file=self.save_file))
        for _ in range(12):
            natio_ = generate_nationality(self.country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            self.squad["midfielder"].append(Player(name_, natio_, randint(16,37), pos_,  current_club=self.name, shirt_number=number, club_coeff=self.coeff, save_file=self.save_file))
        for _ in range(6):
            natio_ = generate_nationality(self.country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Center Forward', 'Second Striker', 'Winger'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            self.squad["attacker"].append(Player(name_, natio_, randint(16,37), pos_,  current_club=self.name, shirt_number=number, club_coeff=self.coeff, save_file=self.save_file))
        
        if not skip_db:
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
        for player in self.bench:
            players.append(player.return_stats())
        for player in self.unrelated:
            players.append(player.return_stats())

        return pd.DataFrame(players, index=None, columns=['Name','Position','MP','GS','A','Avg'])

    def show_formation(self):
        print(f"FORMATION: {self.formation}\n")

        print("STARTING ELEVEN\n")
        for player in self.start_eleven:
            player.basic_info()

        print("BENCH\n")
        for player in self.bench:
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

        self.bench.append(cp_squad['goal_keeper'][1])
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
            self.bench.append(cp_squad['defender'][0])
            self.bench.append(cp_squad['midfielder'][0])
            self.bench.append(cp_squad['attacker'][0])

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

    def __init__(self, name, nationality, age, position, current_club=None, shirt_number=None, club_coeff=65, save_file=None):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.overall = randint(50, club_coeff)
        self.current_club = current_club
        self.position = position
        self.shirt_number = shirt_number
        self.save_file = save_file

        #stats de competição
        self.matches_played = 0
        self.goals = 0
        self.assists = 0
        self.points = 0  # every match another point is add here, thent is calculated by the average
        self.avg = self.average()

    def average(self):
        try:
            self.avg = self.points / self.matches_played
        except:
            self.avg = 0

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
        ls = [ self.name, self.nationality, self.age, self.overall, self.current_club, self.position, self.matches_played, self.goals, self.assists, self.avg, self.save_file ]

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO player (name, nationality, age, overall, current_club, position, matches_played, goals, assists, avg, save_file) VALUES (?,?,?,?,?,?,?,?,?,?,?)", ls)

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

        ls = [ self.name, self.location, self.capacity, self.club_owner ]

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO stadium (name, location, capacity, club_owner) VALUES (?,?,?,?)", ls)

        conn.commit()
        conn.close()