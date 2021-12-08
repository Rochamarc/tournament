import csv 
import sqlite3
import pandas as pd

from database import DomesticLeague, InternationalCup

league = DomesticLeague()
inter = InternationalCup()

class Ranking:
    @staticmethod
    def define_conmebol_points(clubs):
        with open('ranking_conmebol.csv') as file:
            lines = file.readlines() 
            for club in clubs:

                for line in lines:
                    line = line.split(',')
                    if line[0] == club.name:
                    
                        val = line[-1] 
                        val.replace('\n', '')
                        val = float(val)

                        club.ranking_points += val    

    @staticmethod
    def individual_leaderboard(all_clubs, category, season, save_file=None):
        """ Return a dataframe contains name, current_club, position, matches_played, goals, assists, average """
        
        series_data = []

        if category == 'Best Player':
            stats = ['Avg','MP','Goal','Assist']
        elif category == 'Top Scorer':
            stats = ['Goal', 'MP']
        elif category == 'Assists':
            stats = ['Assist', 'MP']

        for club in all_clubs:
            """ add players to series_data """
            series_data += [ player.get_stats() for player in club.start_eleven ] 
            series_data += [ player.get_stats() for player in club.bench ]

        df = pd.DataFrame(series_data, index=None, columns=['Name', 'Club','Position','MP','Goal','Assist','Avg'])
        sorted_data_frame = df.sort_values(by=stats, axis=0, ascending=False)

        if save_file:
            sorted_data_frame.to_csv(f"./files/{save_file}/{category}_{season}.csv")
        return sorted_data_frame[:10]

    @staticmethod 
    def domestic_table(division, season):
        ''' 
        Return a panda series with the tables below
        Position    Club    Matches    Won  Draw    Lost   Goals For    Goals Away    Goals Diff    Points
        '''
        value = league.get_domestic_cup_table(division, season)
        
        df = pd.DataFrame(value, index=None, columns=['id','Club','Matches','Won','Draw','Lost','GF','GA','GD','Points'])
        
        return df

    @staticmethod
    def international_group_table(season):
        ''' 
        Return a panda series with the group stage tables
        '''
        value = inter.get_group_stage_data('2021')
        dfs = []

        for group, data in value.items():
            print('\n')
            print(f"Conmebol Libertadores Group {group}")
            df = pd.DataFrame(data, index=None, columns=['id', 'Club', 'Matches', 'Won', 'Draw', 'Lost', 'GF', 'GA', 'GD', 'Points'])
            print(df)
            print('\n')
            dfs.append(df)
        
        return dfs
    
    @staticmethod
    def player_info(players):
        '''
        Return a squad dataframe from the players inside the club
        '''

        cols = ['id', 'name', 'nationality', 'age', 'overall', 'club', 'position', 'matches played', 'goals', 'assists', 'points', 'average', 'save_file']
        
        df = pd.DataFrame(players, index=None, columns=cols)

        return df
