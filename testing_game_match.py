from classes import *
from game_match import subs 

from random import choice 

river = Club('River Plate', 'Argentina')
river.register_squad()
river.formation_auto()

print(f"""

Formacao dentro do objeto antes do jogo
Titulares: {river.start_eleven}
Reservas: {river.bench}
Nao relacionados: {river.unrelated}

""")

# maneira correta de usar 
start = river.start_eleven.copy()
bench = river.bench.copy()

r_subs = 3

for _ in range(90):
    sub_ = None
    if r_subs > 0:
        sub_ = choice([False, True])

    if sub_:
        sub_conf = subs(start, bench, verbose=True) # return true or false
        if sub_conf:
            r_subs -= 1


print(f"""

Titulares e reservas apos o jogo
{start}
{bench}

""")


print(f"""

Formacao dentro do objeto apos o jogo
Titulares: {river.start_eleven}
Reservas: {river.bench}

""")