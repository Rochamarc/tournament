from random import choice, randint
from pprint import pprint
import pandas as pd
import os
import sqlite3
from name_nationality import *


class Club:

    def __init__(self,name,country,club_class,state=None,save_file=None):
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()
        self.state = state
        self.club_class = club_class
        self.ranking_points = 0
        self.min_coeff = 0
        self.max_coeff = 0
        self.save_file = save_file
        
        # The next attr are refering to handle the squad
        self.formation = None
        self.start_eleven = []
        self.bench = []

        self.stadium = None 

        self.generate_coeff()
        
    def __repr__(self):
        return f"Club({self.name})"

    @property
    def overall(self):
        ''' Define the club overall on the average of player overall '''
        players = sum([ player.overall for player in self.start_eleven ] + [ player.overall for player in self.bench ]) 
        return ( players / len(players) ) 

    
    def get_data(self):
        ''' Return a list with name, country, state, coeff, club_class '''
        return [self.name, self.country, self.state, self.max_coeff, self.club_class, self.formation ]

    def set_formation(self, players_list):
        ''' Receive a list of players 

            id | name | nationality | age | overall | club | position | matches_played | goals | assists | points | avg | save_file
        '''

        squad = []

        # reconstitute players
        for player in players_list:
            name = player[1]
            nation = player[2]
            age = player[3]
            overall = player[4]
            club = player[5]
            posi = player[6]
            p = Player(name, nation, age, posi, 0, 100, current_club=club)
            p.overall = overall
            squad.append(p)
        
        squad.sort(key=lambda player : player.overall) # Sorting items by overall not reverse

        if not self.formation : self.formation = choice(['3-5-2', '4-3-3', '4-4-2']) # set formation if false

        keepers = [ player for player in squad if player.position == 'GK' ]
        backs = [ player for player in squad if player.position in ['CB','RB','LB'] ]
        midfielders = [ player for player in squad if player.position in ['DM','CM','AM'] ]
        attackers = [ player for player in squad if player.position in ['CF','SS','WG'] ]

        forma = [ int(i) for i in self.formation.replace('-', ' ').split(' ') ]
            
        self.start_eleven.append(keepers.pop())

        for _ in range(forma[0]):
            self.start_eleven.append(backs.pop())
        for _ in range(forma[1]):
            self.start_eleven.append(midfielders.pop())
        for _ in range(forma[2]):
            self.start_eleven.append(attackers.pop())
        

        self.bench.append(keepers.pop())
        for i in range(2):
            self.bench.append(backs.pop())
            self.bench.append(midfielders.pop())
            self.bench.append(attackers.pop())


    def generate_coeff(self):
        minimum = 55
        maximum = 60
        
        if self.club_class == 'D':
            minimum -= 12 # 43
            maximum -= 5 # 55
        elif self.club_class == 'C':
            minimum -= 10 # 45
            maximum += 0 # 60
        elif self.club_class == 'B':
            minimum += 5 # 60
            maximum += 10 # 70
        elif self.club_class == 'A':
            minimum += 15 # 70
            maximum += 25 # 85
        else:
            raise NameError(self.club_class, " doesnt match!")        
        
        # update values
        self.min_coeff = minimum
        self.max_coeff = maximum
        return True 

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



#### Player Base Object #####
class Player:

    def __init__(self, name, nationality, age, position, min_coeff, max_coeff, current_club=None, shirt_number=None, save_file=None):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.overall = randint(min_coeff, max_coeff)
        self.current_club = current_club
        self.position = position
        self.shirt_number = shirt_number
        self.save_file = save_file

        #stats de competição
        self.matches_played = 0
        self.goals = 0
        self.assists = 0
        self.points = 0  # every match another point is add here, thent is calculated by the average
    
    @property
    def avg(self):
        try:
            return (round((self.points / self.matches_played), 1))
        except:
            return 0

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

    def get_data(self):
        ''' 
        return list[name, nationality, age, overall, current_club, position, matches, goals, assists, avg]
        '''
        
        return [
            self.name, self.nationality, self.age, self.overall, self.current_club,
            self.position, self.matches_played, self.goals, self.assists, self.avg
        ]


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

    def get_data(self):

        return [ self.name, self.location, self.capacity, self.club_owner ]