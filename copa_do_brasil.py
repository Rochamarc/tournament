from cup import Cup
from draw import Draw

# Exemple of 32 clubs, i'll move on to 64 after this is working correctly

draw = Draw()


matches = draw.national_draw(32) # get all the national clubs

# Round of 32
c = Cup('Copa do Brasil', 2021, 'Round of 32', matches)

c.show()
# TEST
input("Continuer") # Show table

winners = c.run() 

print(winners)

# Round of 16
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Round of 16', matches)

c.show()
# TEST
input("Continuer")

winners = c.run() 

print(winners)
input("Continue")

# Quarter
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Quarter', matches)

c.show()
# TEST
input("Continuer")

winners = c.run() 

print(winners)
input("Continue")

# Semi Finals
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Semi Finals', matches)

c.show()
# TEST
input("Continuer")

winners = c.run() 

print(winners)
input("continue:")

# Finals
matches = draw.basic_draw(winners)

c = Cup('Copa do Brasil', 2021, 'Final', matches)

c.show()
# TEST
input("Continuer")

winners = c.run() 

print(winners)
input("continue:")

