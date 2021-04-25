import csv 
import sqlite3

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
    
    