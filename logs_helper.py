from classes.club import Club 


class LogsHandler:
    @staticmethod
    def get_game_stats(logs: dict, home: Club, away: Club) -> list:
        ''' Return the game stats from logs '''

        logs['game_stats'][home.name]['club_id'] = home.id
        logs['game_stats'][away.name]['club_id'] = away.id

        return logs['game_stats']
    
    @staticmethod
    def prepare_game_stats_logs_to_db(logs: dict) -> list[list]:
        ''' Convert logs dict to data to be inserted on database '''
        data = []

        for _, items in logs.items():
            data.append([
                items['goals'],
                items['shots'],
                items['shots on target'],
                items['fouls'],
                items['tackles'],
                items['stolen_balls'],
                items['saves'],
                items['ball possession'],
                items['offsides'],
                items['free kicks'],
                items['penalties'],
                items['club_id']
            ])

        return data

    @staticmethod
    def prepare_game_logs_to_db(logs: dict, game_stats_id: list) -> list:
        ''' Convert logs dict to data to be inserted on database '''
        conditions = logs['field']['conditions']
        
        return [
            conditions['season'],
            conditions['hour'],
            conditions['climate'],
            conditions['weather'],
            logs['field']['stadium'],
            logs['field']['audience'],
            logs['finances']['ticket_price'],
            game_stats_id[0],
            game_stats_id[1]
        ]

    @staticmethod
    def prepare_championships_logs_to_db(logs: dict, club: int, season: int) -> list:
        ''' 
        Convert and prepare the logs to insert a chmapionships table 
        return [ win, loss, draw, home_goals, away_goals, goals_diff, club_id, season ]
        '''

        data = []

        if logs['others']['draw']:
            data += [0,0,1]
        elif logs['others']['winner'] == club:
            data += [1,0,0]
        else:
            data += [0,1,0]

        data.append(logs['others']['home_goals'])
        data.append(logs['others']['away_goals'])
        data.append(data[0] - data[1])

        data.append(club.id)
        data.append(season)

        return data