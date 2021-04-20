import csv 

with open('ranking_conmebol.csv') as file:
    lines = file.readlines() # isso é uma lista de strings

    for line in lines:
        line = line.split(',')
        val = line[-1] 
        val.replace('\n', '')
        val = float(val)
        del line[-1]
        line.append(val)
        print(line)

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

