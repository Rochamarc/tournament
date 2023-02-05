from cup import Cup
from db.database import CompetitionData
from draw import Draw

# Exemple of 32 clubs, i'll move on to 64 after this is working correctly

draw = Draw()
competition = CompetitionData()

matches = draw.national_draw(32) # get all the national clubs

# Round of 32
c = Cup('Copa do Brasil', 2021, 'Round of 32', matches)

c.show()
# TEST
 # Show table

winners = c.run() 

print(winners)

# Round of 16
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Round of 16', matches)

c.show()
# TEST


winners = c.run() 

print(winners)


# Quarter
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Quarter', matches)

c.show()
# TEST


winners = c.run() 

print(winners)

# Semi Finals
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Semi Finals', matches)

c.show()
# TEST


winners = c.run() 

print(winners)


# Finals
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Final', matches)

c.show()
# TEST


winners = c.run() 

print(winners)


def run_cup(_round, competition, season, winners=None):
    if _round == 'Round of 32': 
        matches = draw.national_draw(32)
    else:
        matches = draw.basic_draw(winners)

    c = Cup(competition, season, _round, matches)

    return c.run()


competition.insert_champion_db('Copa do Brasil', winners[0].name, '2021')

