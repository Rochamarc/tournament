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