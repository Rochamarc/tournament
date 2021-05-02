import csv 
import sqlite3
import pandas as pd 
from datetime import datetime 

# This will became a class Ranking: with static methods
#
#

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

def upload_ranking_db():
    with open('ranking_conmebol.csv') as file:
        lines = file.readlines() # isso é uma lista de strings
    
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        for line in lines:
            line = line.split(',')
            val = line[-1] 
            val.replace('\n', '')
            val = float(val)
            del line[-1]
            line.append(val)
    
            cursor.execute("""
            INSERT INTO clubs_ranking (name, country, points) VALUES (?,?,?)
            """, line)
    
            conn.commit()

        print("Conmebol ranking upload succesfully!")
        conn.close()    

def players_podium(all_clubs, category, season, save_file=None):
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
        series_data += [ player.return_stats() for player in club.start_eleven ] 
        series_data += [ player.return_stats() for player in club.bench ]

    df = pd.DataFrame(series_data, index=None, columns=['Name', 'Club','Position','MP','Goal','Assist','Avg'])
    sorted_data_frame = df.sort_values(by=stats, axis=0, ascending=False)

    sorted_data_frame.to_csv(f"./files/{save_file}/{category}_{season}.csv")
    return sorted_data_frame[:10]

def update_player_stats(all_clubs):
    """ Update players stats Return void """

    for club in all_clubs:
        for player in club.start_eleven : player.average() # update average
        for player in club.bench : player.average() # update average

