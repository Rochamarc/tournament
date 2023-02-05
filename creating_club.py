from classes.club import Club

name = input("Type your club name: ")
country = "Brazil"
state = input("Type your club state: ")
club_class = "D"

club = Club(name, country, club_class, state=state)


