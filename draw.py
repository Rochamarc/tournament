from pprint import pprint 
import random

from classes_helper import GenerateClass

generate = GenerateClass()

class Draw:
    @staticmethod 
    def basic_draw(clubs):
        random.shuffle(clubs)

        return [ [ clubs.pop(), clubs.pop() ] for _ in range(len(clubs) // 2) ]
        
    @staticmethod 
    def national_draw(n_clubs=None):
        bra = generate.reconstruct_international_clubs('BRA')
        
        random.shuffle(bra)
        
        if n_clubs: bra = bra[:n_clubs]

        return [ [ bra.pop(), bra.pop() ] for _ in range(len(bra)//2) ]

    @staticmethod
    def international_draw():
        arg = generate.reconstruct_international_clubs('ARG')
        bol = generate.reconstruct_international_clubs('BOL')
        chi = generate.reconstruct_international_clubs('CHI')
        col = generate.reconstruct_international_clubs('COL')
        equ = generate.reconstruct_international_clubs('EQU')
        par = generate.reconstruct_international_clubs('PAR')
        per = generate.reconstruct_international_clubs('PER')
        uru = generate.reconstruct_international_clubs('URU')
        ven = generate.reconstruct_international_clubs('VEN')

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
        for i in range(6):
            # liber
            libertadores.append(arg.pop())
            # suda
            sudamericana.append(arg.pop())

        for i in range(4):
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

