from random import choice 

def game_match(match_round, competition, home_team, away_team, verbose=False):
    # stadium = home_team.stadium 
    hour = choice(['19:00', '21:00', '19:15'])
    weather = choice(['Limpo', 'Nublado', 'Chuvoso'])
    game_stats = {
        "competition": competition,
        "round": match_round,
        "hour": hour,
        # "location": stadium.location,
        "home_team": home_team,
        "away_team": away_team,
        "conditions": weather
    }

    if verbose:
        print(f"""
Competition: {competition}
Round: {match_round}

Hour: {hour}
Conditions: {weather}
{home_team.name.upper()} ({home_team.short_country}) x {away_team.name.upper()} ({away_team.short_country})
    """)

    goals = match_actions(home_team, away_team, 90) # start match 

    home_goals = goals['home_goal']
    away_goals = goals['away_goal']

    """ You only have to register their goals and theis oponent goals and the object define if its a win, lose or draw """
    home_team.register_game(home_goals, away_goals)
    away_team.register_game(away_goals, home_goals)

    game_stats['home_goals'] = home_goals
    game_stats['away_goals'] = away_goals

    print(f"""
Round: {match_round}
Competition: {competition}
{home_team.name.upper()} ({home_team.short_country}) {home_goals} x {away_goals} {away_team.name.upper()} ({away_team.short_country})
    """)

    return game_stats

def match_actions(home_team, away_team, match_time):
    """ Receive home players and return a dict with home_goal away_goal """
    
    home_goal = 0
    away_goal = 0
    
    home_subs = 3
    away_subs = 3

    home_players = [ player for player in home_team.start_eleven ]
    away_players = [ player for player in away_team.start_eleven ]

    home_bench = [ player for player in home_team.bench ]
    away_bench = [ player for player in away_team.bench ]

    basic_stats = [ True, False, False, False, False, False ] # 1 in 6 chances

    if match_time == 90:

        for player in home_players:
            player.matches_played += 1
            player.points += 4.0   

        for player in away_players:
            player.matches_played += 1
            player.points += 4.0

    
    for i in range(match_time):
        if i % 2 == 0:

            # defensives
            keeper = select_player(away_players, 'goalkeeper')
            defensor = select_player(away_players, 'defender')

            # attackers
            midfielder = select_player(home_players, 'midfielder')
            attacker = select_player(home_players, 'attacker')

            """ Ataque = toca + chuta """
            """ Defesa = corta + defende """

            touch = choice(basic_stats + [ True for _ in range((midfielder.overall // 9) //2) ])
            tackle = choice(basic_stats + [ True for _ in range((defensor.overall // 9) // 2) ])

            # substitution
            if home_subs > 0:
                sub = choice([True, False])
                
                if sub:
                    confirm_sub = subs(home_players, home_bench)

                    if confirm_sub:
                        home_subs -= 1

            if tackle:
                """ defender success """
                defensor.points += 0.7 # clearence
            else:
                if touch:
                    """ touch sucess """
                    midfielder.points += 0.5 # pass 

                    finish = choice(basic_stats + [ True for _ in range((attacker.overall // 9) // 2) ])
                    defense = choice(basic_stats + [ True for _ in range((keeper.overall // 9) // 2) ])

                    if defense:
                        """ keeper sucess """
                        keeper.points += 0.8 # defense
                    else:
                        if finish:
                            """ goal """ 
                            assist = choice([True,False])

                            if assist:
                                """ goal with assist """
                                midfielder.points += 1.0 # assist
                                midfielder.assists += 1 

                            home_goal += 1
                            attacker.points += 1.4 # goals 
                            attacker.goals += 1
                            keeper.points -= 0.9 # conceded
                            defensor.points -= 0.6 # conceded
        else:
            # defensives
            keeper = select_player(home_players, 'goalkeeper')
            defensor = select_player(home_players, 'defender')

            # attackers
            midfielder = select_player(away_players, 'midfielder')
            attacker = select_player(away_players, 'attacker')


            """ Ataque = toca + chuta """
            """ Defesa = corta + defende """

            touch = choice(basic_stats + [ True for _ in range((midfielder.overall // 9) // 2) ])
            tackle = choice(basic_stats + [ True for _ in range((defensor.overall // 9) // 2) ])

            # substitution
            if away_subs > 0:
                sub = choice([True, False])
                
                if sub:
                    confirm_sub = subs(away_players, away_bench)

                    if confirm_sub:
                        away_subs -= 1

            if tackle:
                """ defender success """
                defensor.points += 0.7 # clearence
            else:
                if touch:
                    """ touch sucess """
                    midfielder.points += 0.5 # pass 

                    finish = choice(basic_stats + [ True for _ in range((attacker.overall // 9) // 2) ])
                    defense = choice(basic_stats + [ True for _ in range((keeper.overall // 9) // 2) ])

                    if defense:
                        """ keeper sucess """
                        keeper.points += 0.8 # defense
                    else:
                        if finish:
                            """ goal """ 
                            assist = choice([True,False])

                            if assist:
                                """ goal with assist """
                                midfielder.points += 1.0 # assist
                                midfielder.assists += 1 

                            away_goal += 1
                            attacker.points += 1.4 # goals 
                            attacker.goals += 1
                            keeper.points -= 0.9 # conceded
                            defensor.points -= 0.6 # conceded
                     
    return { 'home_goal': home_goal, 'away_goal': away_goal }

def subs(starting, bench, verbose=False):
    player_out = choice(starting)
    options = []
    for p in bench:
        if 'Back' in p.position and 'Back' in player_out.position:
            options.append(p)
        elif 'Midfielder' in p.position and 'Midfielder' in player_out.position:
            options.append(p)
        elif p.position in ['Center Forward', 'Second Striker', 'Winger'] and player_out.position in  ['Center Forward', 'Second Striker', 'Winger']:
            options.append(p)
        elif p.position == 'Goalkeeper' and player_out.position == 'Goalkeeper':
            options.append(p)
    
    if options:
        return False 
    
    player_in = choice(options) # select the player
    starting.remove(player_out) # out
    bench.remove(player_in) # out from the bench
    player_in.points += 1.5 # add some points
    player_in.matches_played += 1
    starting.append(player_in) # into the pitch

    if verbose:
        print(f"In: {player_in} {player_in.position}")
        print(f"Out: {player_out} {player_in.position}")

    return True
    

def select_player(start_eleven, position):
    player = None
    l_choice = []

    if position == 'goalkeeper':
        for p in start_eleven:
            if p.position == 'Goalkeeper':
                player = p
    elif position == 'defender':
        player = choice([ p for p in start_eleven if p.position in ['Center Back', 'Right Back', 'Left Back']])        
    elif position == 'midfielder':
        player = choice([ p for p in start_eleven if p.position in ['Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder']])        
    elif position in 'attacker':
        player = choice([ p for p in start_eleven if p.position in ['Center Forward', 'Second Striker', 'Winger']])        

    return player 