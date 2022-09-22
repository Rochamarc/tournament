from classes_helper import GenerateClass

generate = GenerateClass()

class Cup:
    def __init__(self, competition_name, season):
        self.competition_name = competition_name
        self.season = season

    def run(self):
        arg = generate.reconstruct_international_clubs('ARG')
        bol = generate.reconstruct_international_clubs('BOL')
        chi = generate.reconstruct_international_clubs('CHI')
        col = generate.reconstruct_international_clubs('COL')
        equ = generate.reconstruct_international_clubs('EQU')
        par = generate.reconstruct_international_clubs('PAR')
        per = generate.reconstruct_international_clubs('PER')
        uru = generate.reconstruct_international_clubs('URU')
        ven = generate.reconstruct_international_clubs('VEN')


Cup('Libertadores', '2021').run()