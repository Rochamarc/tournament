# Testing new queries
from random import randint, choice

import mysql.connector

database_config = {
    "host": "localhost",
    "user": "tournament_user",
    "password": "tournament_pass",
    "database": "tournament_test"
}

conn = mysql.connector.connect(**database_config)
cursor = conn.cursor()

positions = ['CB','LB','RB','DM','CM','AM','SS','CF']

def get_skill_by_position(position: str) -> list[int]:
    '''Define a list of values based on player position 
    
    Parameters
    ----------
    position : str
        Argument that defines how his skills are gonna be calculated

    Returns
    -------
        A list of integer values
    '''
    
    if position in ['CB','LB','RB','DM']:
        return [ randint(55,99) for _ in range(3) ] + [ randint(35,85) for _ in range(3)]
    return [ randint(35,85) for _ in range(3) ] + [ randint(55,99) for _ in range(3) ]

for i in range(30):
    name = 'Player {}'.format(i)
    position = choice(positions)

    cursor.execute('INSERT INTO player VALUES(NULL, %s, %s);', [name, position])
    conn.commit()    

    cursor.execute('SELECT id FROM player ORDER BY(id) DESC LIMIT 1;')
    id = cursor.fetchall()

    id = id[0][0]

    skills = get_skill_by_position(position)
    skills.append(id)

    insert_query = """
    INSERT INTO player_skill (tackle, strength, passing, dribling, finish, penalty, player_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    print(skills)

    cursor.execute(insert_query , skills)
    conn.commit()



conn.close()