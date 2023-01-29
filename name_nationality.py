from random import choice

class NameAndNationality:
    @staticmethod
    def generate_nationality(team_nationality):
        ''' Generates the player nationality '''
        outsider_prob = choice([True, False, False, False, False, False])

        south = ['BRA', 'ARG', 'URU', 'EQU', 'PER', 'CHI', 'VEN', 'PAR', 'BOL', 'GUI', 'PAN']

        if outsider_prob:
            # gringo
            return choice(south)
        return team_nationality

    @staticmethod 
    def generate_name(nationality):
        ''' Generates a name based on the player nationality '''
        if nationality == 'BRA':
            first_name = choice(NameAndNationality().access_file('first_name_br.csv'))
            last_name = choice(NameAndNationality().access_file('last_name_br.csv')) 
            names = [first_name, last_name]
        else:
            first_name = choice(NameAndNationality().access_file('first_name_g.csv'))
            last_name = choice(NameAndNationality().access_file('last_name_g.csv'))
            names = [first_name, last_name]

        return ' '.join(names)
    
    @staticmethod
    def access_file(file):
        ''' Open the name files in files/names '''
        with open(f'files/names/{file}', encoding='utf8') as f:
            return [ line.replace('\n', '') for line in f.readlines() ]

if __name__ == '__main__':
    print(NameAndNationality().generate_name(''))
