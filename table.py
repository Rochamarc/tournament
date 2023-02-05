from random import randint, choice

from db.database import DomesticLeague

domestic = DomesticLeague()

class Table:
    @staticmethod
    def define_schedule(clubs,stadiums):
        '''
        Return a dict of lists with all the rounds filled with
        [ home_club, away_club, stadium ]
        '''

        # Not properly working yet
        # need to add max of 10 matches per round
        # and tha same club doesnt play two or more times per round
        # and the stadium cant have two or more matcher per round
        # now the method doesnt have any limitation
        # and the method will return a dict of Game() lists not list of listss

        schedule = {}

        rounds = {}
        for i in range(1,39):
            rounds[f'Round {i}'] = []

        for clb in clubs:
            ''' Define a schedule '''
            schedule[clb] = [ club for club in clubs if club.name != clb.name ]

        for home_club, away_clubs in schedule.items():
            for away_club in away_clubs:
                rnd = randint(1,38)
                rounds[f'Round {rnd}'].append([home_club, away_club, choice(stadiums)])

        return rounds 

    @staticmethod 
    def get_international_classified(season, competition):
        previous_season = str(int(season) - 1) # get the previous season

        previous_serie_a = domestic.get_domestic_cup_table('serie_a', previous_season)

        if competition == 'libertadores':
            return { 'group_stage': previous_serie_a[:4], 'pre_libertadores': previous_serie_a[4:6] }
        return { 'sudamericana': previous_serie_a[7:12] }

    @staticmethod 
    def promotions_and_relegations(season, verbose=False):
        ''' Promove and relegates all the divisions of the domestic league
            return a dict with the promoted and relegated clubs
        '''
        previous_season = str(int(season) - 1) # get the previous season

        previous_serie_a = domestic.get_domestic_cup_table('serie_a', previous_season)
        previous_serie_b = domestic.get_domestic_cup_table('serie_b', previous_season)
        previous_serie_c = domestic.get_domestic_cup_table('serie_c', previous_season)

        domestic.create_domestic_table('serie_a', season) # create next season table
        domestic.create_domestic_table('serie_b', season) # create next season table
        domestic.create_domestic_table('serie_c', season) # create next season table

        current_serie_a = [ previous_serie_a[i][1] for i in range(16) ] # first 16 teams from serie_a
        current_serie_b = [ previous_serie_b[i][1] for i in range(4,16) ] # 5 to 16 from serie b
        current_serie_c = [ previous_serie_c[i][1] for i in range(4,20) ] # 5 to 20 from serie c
        
        promotions = {
            'serie_a': [],
            'serie_b': []
        }
        relegations = {
            'serie_b': [],
            'serie_c': []
        }

        for i in range(4):
            ''' promotions '''
            current_serie_a.append(previous_serie_b[i][1]) # get the first four clubs from serie b ||  b -> a
            current_serie_b.append(previous_serie_c[i][1]) # get the first four clubs from serie c ||  c -> b

            ''' relegations'''
            relegated_b = previous_serie_a.pop()
            relegated_c = previous_serie_b.pop() 

            current_serie_b.append(relegated_b[1]) # get the last four from serie b || a -> b
            current_serie_c.append(relegated_c[1]) # get the last four from serie c || b -> c

            if verbose:
                promotions['serie_a'].append(previous_serie_b[i])
                promotions['serie_b'].append(previous_serie_c[i])

                relegations['serie_b'].append(relegated_b)
                relegations['serie_c'].append(relegated_c)

        
        domestic.domestic_table_basic(current_serie_a, 'serie_a', season, verbose=verbose)
        domestic.domestic_table_basic(current_serie_b, 'serie_b', season, verbose=verbose)
        domestic.domestic_table_basic(current_serie_c, 'serie_c', season, verbose=verbose)

        return { 'promotions': promotions, 'relegations': relegations }