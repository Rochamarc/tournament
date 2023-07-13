from random import randint, choice

class NameAndNationality:
    @staticmethod
    def generate_nationality(team_nationality):
        ''' Generates the player nationality '''
        outsider_prob = randint(1,6)

        south = ['BRA', 'ARG', 'URU', 'EQU', 'PER', 'CHI', 'VEN', 'PAR', 'BOL', 'GUI', 'PAN']

        if outsider_prob == 1:
            return choice(south)
        return team_nationality

    @classmethod 
    def generate_name(cls, nationality):
        ''' Generates a name based on the player nationality '''
        
        first_name = choice(cls.access_file('first_name_br.csv')) if nationality == 'BRA' else choice(cls.access_file('first_name_g.csv'))
        last_name = choice(cls.access_file('last_name_br.csv')) if nationality == 'BRA' else choice(cls.access_file('last_name_g.csv'))
        names = [first_name, last_name]
        
        return ' '.join(names)
    
    @staticmethod
    def access_file(file):
        ''' Open the name files in files/names '''
        with open(f'files/names/{file}', encoding='utf8') as f:
            return [ line.replace('\n', '') for line in f.readlines() ]

if __name__ == '__main__':
    print(NameAndNationality().generate_name(''))
