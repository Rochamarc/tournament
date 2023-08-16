import random

from helper import Helper

helper = Helper()

class Draw:
    @staticmethod 
    def basic_draw(clubs: list) -> list:
        ''' Return a draw with a given list of clubs '''
        random.shuffle(clubs)

        return [ [ clubs.pop(), clubs.pop() ] for _ in range(len(clubs) // 2) ]
        
    @staticmethod 
    def national_draw(n_clubs:int=None) -> list:
        ''' Get a national clubs draw '''
        bra = helper.reconstruct_international_clubs('BRA')
        
        random.shuffle(bra)
        
        if n_clubs: bra = bra[:n_clubs]

        return [ [ bra.pop(), bra.pop() ] for _ in range(len(bra)//2) ]

    @staticmethod
    def international_draw() -> dict:
        ''' Return sudamericana and libertadores draw '''
        
        arg = helper.reconstruct_international_clubs('ARG')
        bol = helper.reconstruct_international_clubs('BOL')
        chi = helper.reconstruct_international_clubs('CHI')
        col = helper.reconstruct_international_clubs('COL')
        equ = helper.reconstruct_international_clubs('EQU')
        par = helper.reconstruct_international_clubs('PAR')
        per = helper.reconstruct_international_clubs('PER')
        uru = helper.reconstruct_international_clubs('URU')
        ven = helper.reconstruct_international_clubs('VEN')

        random.shuffle(arg)
        random.shuffle(bol)
        random.shuffle(chi)
        random.shuffle(col)
        random.shuffle(equ)
        random.shuffle(par)
        random.shuffle(per)
        random.shuffle(uru)
        random.shuffle(ven)

        libertadores = []
        sudamericana = []

        # HERE im gonna take the 6 higher positions to libertadores
        # and the 7th to 14th position from the brasileirao to the other positions

        # draw
        for _ in range(6):
            # liber
            libertadores.append(arg.pop())
            # suda
            sudamericana.append(arg.pop())

        for _ in range(4):
            # liber
            libertadores.append(bol.pop())
            libertadores.append(chi.pop())
            libertadores.append(col.pop())
            libertadores.append(equ.pop())
            libertadores.append(par.pop())
            libertadores.append(per.pop())
            libertadores.append(uru.pop())
            libertadores.append(ven.pop())
            # suda
            sudamericana.append(bol.pop())
            sudamericana.append(chi.pop())
            sudamericana.append(col.pop())
            sudamericana.append(equ.pop())
            sudamericana.append(par.pop())
            sudamericana.append(per.pop())
            sudamericana.append(uru.pop())
            sudamericana.append(ven.pop())
        
        return { "Libertadores": libertadores, "Sudamericana": sudamericana }

