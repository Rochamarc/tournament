from random import choice

class NameAndNationality:
    @staticmethod
    def generate_nationality(team_nationality):
        outsider_prob = choice([True, False, False, False, False, False])

        south = ['Brasil', 'Argentina', 'Uruguay', 'Ecuador', 'Peru', 'Chile', 'Venezuela', 'Paraguay', 'Bolivia', 'Guiana', 'Panama']

        if outsider_prob:
            # gringo
            return choice(south)
        return team_nationality

    @staticmethod 
    def generate_name(nationality):
        if nationality == 'Brasil':
            first_name = choice(NameAndNationality().access_file('first_name_br.txt'))
            last_name = choice(NameAndNationality().access_file('last_name_br.txt')) 
        else:
            first_name = choice(NameAndNationality().access_file('first_name_g.txt'))
            last_name = choice(NameAndNationality().access_file('last_name_g.txt'))

        return f'{first_name} {last_name}'
    
    @staticmethod
    def access_file(file):
        with open(f'files/names/{file}', encoding='utf8') as f:
            return [ line.replace('\n', '') for line in f.readlines() ]

if __name__ == '__main__':
    print(NameAndNationality().generate_name(''))