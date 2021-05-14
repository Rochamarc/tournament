from random import choice, randint
from pprint import pprint
import pandas as pd
import os
import sqlite3
from name_nationality import *


class Club:

    def __init__(self,name,country,save_file=None):
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goal_difference = 0
        self.victory = 0
        self.draw = 0
        self.defeat = 0
        self.games_played = 0
        self.overall = 0 
        self.ranking_points = 0
        self.coeff = self.set_coeff()
        self.save_file = save_file
        
        # The next attr are refering to handle the squad
        self.squad = None
        self.formation = None
        self.start_eleven = []
        self.bench = []
        self.unrelated = []

        self.stadium = None 
        
    def __repr__(self):
        return f"Club({self.name})"

    def get_season_stats(self):
        return f"{self.name.upper()}\nGroup Stage Points: {self.points}\nVictory: {self.victory}\nDraws: {self.draw}\nDefeat: {self.defeat}\nGoals Scored: {self.goals_scored}\nGoals Conceded: {self.goals_conceded}\nGoals Diff: {self.goal_difference}"

    def get_stats(self):
        ''' return a list[ name, points, victory, draw, defeat, goal_scored, goals_conceded, goal_balance ] '''
        return [self.name, self.points, self.victory, self.draw, self.defeat, self.goals_scored, self.goals_conceded, self.goal_difference]
    
    def get_df_cast(self):
        ''' return a dataframe with name, position, matches, goals, assists, average points '''

        # get all the players
        players = [ player.get_stats() for player in self.start_eleven ] + [ player.get_stats() for player in self.bench ] + [ player.get_stats() for player in self.unrelated ]

        return pd.DataFrame(players, index=None, columns=['Name','Position','MP','GS','A','Avg'])

    def get_formation(self):
        ''' probably gonna be deleted '''
        print(f"FORMATION: {self.formation}\n")

        print("STARTING ELEVEN\n")
        for player in self.start_eleven:
            print(player.get_info())

        print("BENCH\n")
        for player in self.bench:
            print(player.get_info())

        print("UNRELATAED\n")
        for player in self.unrelated:
            print(player.get_info())

    def set_overall(self):
        ''' Define the club overall on the average of player overall '''
        players = [ player.overall for player in self.start_eleven ] + [ player.overall for player in self.bench ] + [ player.overall for player in self.unrelated ]
        self.overall = sum(players) / len(players) 

    def set_formation(self, squad):
        self.squad = squad

        # sorting squad
        for key, value in self.squad.items():
            value.sort(key=lambda player: player.overall, reverse=True)

        cp_squad = self.squad.copy()

        self.formation = choice(['3-5-2', '4-3-3', '4-4-2'])

        self.start_eleven.append(cp_squad['goal_keeper'][0])
        del cp_squad['goal_keeper'][0]

        self.bench.append(cp_squad['goal_keeper'][1])
        del cp_squad['goal_keeper'][0]

        forma = [ int(i) for i in self.formation.replace('-', ' ').split(' ') ]
            
        for _ in range(forma[0]):
            self.start_eleven.append(cp_squad['defender'][0])
            del cp_squad['defender'][0]
        for _ in range(forma[1]):
            self.start_eleven.append(cp_squad['midfielder'][0])
            del cp_squad['midfielder'][0]
        for _ in range(forma[2]):
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
        self.set_overall()

    def set_coeff(self):
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

    """ this should not be here, this is a stats function not an club """
    def register_game(self, goals_scored, goals_conceded, match_type):
        ''' match type group_stage or knock_out '''
        if goals_scored > goals_conceded:
            if match_type == 'group_stage' : self.points += 3 
            self.victory += 1
        if goals_scored == goals_conceded:
            if match_type == 'group_stage' :  self.points += 1
            self.draw += 1
        if goals_scored < goals_conceded:
            self.defeat += 1

        self.set_goal_diff(goals_scored, goals_conceded)

    def set_goal_diff(self, goals_scored, goals_conceded):
        self.games_played += 1
        self.goals_scored += goals_scored
        self.goals_conceded += goals_conceded
        self.goal_difference += goals_scored - goals_conceded

# all the stats players are gonna became self.__ and controlled by the methods with decoractor
#
#

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
        self.avg = self.set_avg()

    def set_avg(self):
        try:
            self.avg = round((self.points / self.matches_played), 1)
        except:
            self.avg = 0

    # Gera o output pro desenvolvedor
    def __repr__(self):
        return f'Player({self.name})'

    # Gera o output para o usuario final
    def __str__(self):
        return f'Player({self.name})'

    def get_short_info(self):
        return f"{self.name} :: {self.overall} \n{self.position}\n"

    def get_info(self):
        return f"Name: {self.name}\nOverall: {self.overall}\nPosition: {self.position}\nCurrent Club: {self.current_club}\nAge: {self.age}\nNationality: {self.nationality}\n"

    def get_stats(self):
        ''' return list[ name, position, matches, goals, assists, average points ] '''
        return [self.name,  self.current_club, self.position, self.matches_played, self.goals, self.assists, self.avg ]

    def get_personal_stats(self):
        ''' return list[ name, position, overall, age ] '''
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

    def __repr__(self):
        return f'Stadium({self.name})'

    def get_info(self):
        return f"\nName: {self.name}\nLocation: {self.location}\nCapacity: {self.capacity}\nOwner: {self.club_owner}\n"

    def db_insertion(self):

        ls = [ self.name, self.location, self.capacity, self.club_owner ]

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO stadium (name, location, capacity, club_owner) VALUES (?,?,?,?)", ls)

        conn.commit()
        conn.close()
