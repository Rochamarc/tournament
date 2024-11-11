from controllers.competitions_controller import CompetitionsController
from controllers.championships_controller import ChampionshipsController
from controllers.club_class_controller import ClubClassController
from controllers.clubs_controller import ClubsController

competitions_controller = CompetitionsController()
championships_contoller = ChampionshipsController()
club_class_controller = ClubClassController()
clubs_controller = ClubsController()

# championships_contoller.insert_championship()

# General Data

competitions = [
    'Campeonato Brasileiro',
    'Liga Profesional de Futbol',
    'Copa do Brasil',
    'Copa Libertadores da America',
]

divisions = [
    'Serie A',
    'Serie B',
    'Serie C',
    'Primera Divison'
]

club_classes = [
    'A',
    'B',
    'C',
    'D'
]

competitions_controller.insert_competitions(competitions=competitions)

club_class_controller.insert_club_classes(club_classes=club_classes)

# Serie A Data
serie_a_clubs = [
    ['América Mineiro', 'Brazil', 2],
    ['Atlético Mineiro', 'Brazil', 1],
    ['Athletico Paranaense', 'Brazil', 2],
    ['Ceará', 'Brazil', 2],
    ['Fortaleza', 'Brazil', 2],
    ['Flamengo', 'Brazil', 1],
    ['Fluminense', 'Brazil', 1],
    ['Cuiabá', 'Brazil', 2],
    ['Grêmio', 'Brazil', 1],
    ['International', 'Brazil', 1],
    ['Chapecoense', 'Brazil', 3],
    ['Juventude', 'Brazil', 3],
    ['São Paulo', 'Brazil', 1],
    ['Corinthians', 'Brazil', 1],
    ['Palmeiras', 'Brazil', 1],
    ['Santos', 'Brazil', 2],
    ['Red Bull Bragantino', 'Brazil', 2],
    ['Sport Recife', 'Brazil', 3],
    ['Bahia', 'Brazil', 2],
    ['Atlético Goianiense', 'Brazil', 2],
]

serie_a_championships = [
    ['2022', 1, 1],
    ['2022', 2, 1],
    ['2022', 3, 1],
    ['2022', 4, 1],
    ['2022', 5, 1],
    ['2022', 6, 1],
    ['2022', 7, 1],
    ['2022', 8, 1],
    ['2022', 9, 1],
    ['2022', 10, 1],
    ['2022', 11, 1],
    ['2022', 12, 1],
    ['2022', 13, 1],
    ['2022', 14, 1],
    ['2022', 15, 1],
    ['2022', 16, 1],
    ['2022', 17, 1],
    ['2022', 18, 1],
    ['2022', 19, 1],
    ['2022', 20, 1],
]

clubs_controller.insert_clubs(serie_a_clubs)

# Serie B Data

serie_b_clubs = [
    [ "Vasco da Gama", 'Brazil', 2],
    [ "Botafogo", 'Brazil', 2],
    [ "Cruzeiro", 'Brazil', 2],
    [ "Operário", 'Brazil', 3],
    [ "Coritiba", 'Brazil', 2],
    [ "Goiás", 'Brazil', 2],
    [ "Guarani", 'Brazil', 3],
    [ "Avaí", 'Brazil', 3],
    [ "CRB", 'Brazil', 3],
    [ "CSA", 'Brazil', 3],
    [ "Náutico", 'Brazil', 3],
    [ "Sampaio Corrêa", 'Brazil', 3],
    [ "Vila Nova", 'Brazil', 3],
    [ "Ponte Preta", 'Brazil', 3],
    [ "Brusque", 'Brazil', 3],
    [ "Remo", 'Brazil', 3],
    [ "Londrina", 'Brazil', 3],
    [ "Vitória", 'Brazil', 3],
    [ "Confiança", 'Brazil', 3],
    [ "Brasil de Pelotas", 'Brazil', 3],
]

serie_b_championships = [
    [ '2022', 21, 2],
    [ '2022', 22, 2],
    [ '2022', 23, 2],
    [ '2022', 24, 2],
    [ '2022', 25, 2],
    [ '2022', 26, 2],
    [ '2022', 27, 2],
    [ '2022', 28, 2],
    [ '2022', 29, 2],
    [ '2022', 30, 2],
    [ '2022', 31, 2],
    [ '2022', 32, 2],
    [ '2022', 33, 2],
    [ '2022', 34, 2],
    [ '2022', 35, 2],
    [ '2022', 36, 2],
    [ '2022', 37, 2],
    [ '2022', 38, 2],
    [ '2022', 39, 2],
    [ '2022', 40, 2],
]

clubs_controller.insert_clubs(serie_b_clubs)


# Serie C Data
serie_c_clubs = [
    [ "Paysandu", "Brazil", 4],
    [ "Tombense", "Brazil", 4],
    [ "Botafogo-PB", "Brazil", 4],
    [ "Manaus", "Brazil", 4],
    [ "Volta Redonda", "Brazil", 4],
    [ "Ferroviário", "Brazil", 4],
    [ "Altos", "Brazil", 4],
    [ "Floresta", "Brazil", 4],
    [ "Jacuipense", "Brazil", 4],
    [ "Santa Cruz", "Brazil", 4],
    [ "Novorizontino", "Brazil", 4],
    [ "Ituano", "Brazil", 4],
    [ "Ypiranga", "Brazil", 4],
    [ "Criciúma", "Brazil", 4],
    [ "Figueirense", "Brazil", 4],
    [ "São José", "Brazil", 4],
    [ "Botafogo SP", "Brazil", 4],
    [ "Mirasol", "Brazil", 4],
    [ "Paraná", "Brazil", 4],
    [ "Oeste", "Brazil", 4],
]

serie_c_championships = [    
    [ '2022', 41, 3],
    [ '2022', 42, 3],
    [ '2022', 43, 3],
    [ '2022', 44, 3],
    [ '2022', 45, 3],
    [ '2022', 46, 3],
    [ '2022', 47, 3],
    [ '2022', 48, 3],
    [ '2022', 49, 3],
    [ '2022', 50, 3],
    [ '2022', 51, 3],
    [ '2022', 52, 3],
    [ '2022', 53, 3],
    [ '2022', 54, 3],
    [ '2022', 55, 3],
    [ '2022', 56, 3],
    [ '2022', 57, 3],
    [ '2022', 58, 3],
    [ '2022', 59, 3],
    [ '2022', 60, 3],
]

clubs_controller.insert_clubs(serie_c_clubs)

argentinian_clubs = [    
    ["River Plate", "Argentina", 2],
    ["Talleres (Córdoba)", "Argentina", 3],
    ["San Lorenzo", "Argentina", 3],
    ["Lanús", "Argentina", 2],
    ["Estudiantes de La Plata", "Argentina", 3],
    ["Defensa y Justicia", "Argentina", 3],
    ["Boca Juniors", "Argentina", 2],
    ["Rosário Central", "Argentina", 3],
    ["Godoy Cruz Antonio Tomba", "Argentina", 3],
    ["Argentinos Juniors", "Argentina", 2],
    ["Atlético Tucumán", "Argentina", 3],
    ["Racing Club", "Argentina", 2],
    ["Belgrano (Córdoba)", "Argentina", 3],
    ["Newell's Old Boys", "Argentina", 3],
    ["Barracas Central", "Argentina", 3],
    ["Tigre", "Argentina", 3],
    ["Platense", "Argentina", 3],
    ["Instituto (Córdoba)", "Argentina", 3],
    ["Sarmiento (Junín)", "Argentina", 3],
    ["Unión (Santa Fe)", "Argentina", 3],
    ["Banfield", "Argentina", 3],
    ["Gimnasia La Plata", "Argentina", 3],
    ["Central Córdoba (Santiago del Estero)", "Argentina", 3],
    ["Independiente", "Argentina", 2],
    ["Vélez Sarsfield", "Argentina", 3],
    ["Huracán", "Argentina", 3],
    ["Colón (Santa Fe)", "Argentina", 3],
    ["Arsenal Sarandi", "Argentina", 3],
]

argentinian_championships = [
    ['2022', 61, 4],
    ['2022', 62, 4],
    ['2022', 63, 4],
    ['2022', 64, 4],
    ['2022', 65, 4],
    ['2022', 66, 4],
    ['2022', 67, 4],
    ['2022', 68, 4],
    ['2022', 69, 4],
    ['2022', 70, 4],
    ['2022', 71, 4],
    ['2022', 72, 4],
    ['2022', 73, 4],
    ['2022', 74, 4],
    ['2022', 75, 4],
    ['2022', 76, 4],
    ['2022', 77, 4],
    ['2022', 78, 4],
    ['2022', 79, 4],
    ['2022', 80, 4],
    ['2022', 81, 4],
    ['2022', 82, 4],
    ['2022', 83, 4],
    ['2022', 84, 4],
    ['2022', 85, 4],
    ['2022', 86, 4],
    ['2022', 87, 4],
    ['2022', 88, 4],

]

clubs_controller.insert_clubs(argentinian_clubs)



# /* GENERIC STADIUMS */
# whitout city

generic_stadiums = [
    [ 'Rei Pelé Arena', 100000 ,'Brazil'],
    [ 'Estádio Porto Alegre', 65000 ,'Brazil'],
    [ 'Estádio Arthur Antunes Coimbra', 70000 ,'Brazil'],
    [ 'Arena do Castelo', 90000 ,'Brazil'],
    [ 'Arena Dom Pedro II', 150000 ,'Brazil'],
    [ 'Estádio do Tupiniquim', 30000 ,'Brazil'],
    [ 'Zumbi dos Palmares', 30000 ,'Brazil'],
    [ 'Arena Princesa Izabel', 62000 ,'Brazil'],
    [ 'Arena Joviedade', 200000 ,'Brazil'],
    [ 'Estádio da Paulista', 150000 ,'Brazil'],
    [ 'Estádio Sertanejo', 120000 ,'Brazil'],
    [ 'Arena Mário Jorge Lobo Zagallo', 70000 ,'Brazil'],
    [ 'Arena João Leite Ortiz', 35000 ,'Brazil'],
]

# /* REAL STADIUMS */
real_stadiums = [
    ["Monumental de la U",80903,"Peru","Lima"],
    ["Maracanã",78838,"Brazil","Rio de Janeiro"],
    ["Mané Garrincha",72788,"Brazil","Brasília"],
    ["Morumbi",72039,"Brazil","Sao Paulo"],
    ["Monumental de Núñez",70074,"Argentina","Buenos Aires"],
    ["Mineirão",61846,"Brazil","Belo Horizonte"],
    ["Arena do Grêmio",60540,"Brazil","Porto Alegre"],
    ["Centenario",60235,"Uruguay","Montevideu"],
    ["Estadio Nacional del Peru",60000,"Peru","Lima"],
    ["Arruda",60044,"Brazil","Recife"],
    ["Estadio Monumental Isidro Romero Carbo",57267,"Ecuador","Guayaquil"],
    ["Estadio Mario Alberto Kempes",57000,"Argentina","Cordoba"],
    ["Estadio La Bombonera",54000,"Argentina","Buenos Aires"],
    ["Municipal João Avelange",53350,"Brazil","Uberlandia"],
    ["Ciudad de La Plata",53000,"Argentina","Buenos Aires"],
    ["Castelão",52552,"Brazil","Fortaleza"],
    ["Deportivo Cali",52000,"Colombia","Cali"],
    ["Monumental de Maturín",51796,"Venezuela","Maturin"],
    ["Presidente Juan Domingo Perón",51389,"Argentina","Buenos Aires"],
    ["Beira-Rio",50842,"Brazil","Porto Alegre"],
    ["Libertadores da America",49592,"Argentina","Buenos Aires"],
    ["José Amalfitani",49540,"Argentina","Buenos Aires"],
    ["Néo Química Arena",49205,"Brazil","Sao Paulo"],
    ["Nacional de Chile",48665,"Chile","Santiago"],
    ["Metropolitano Lara",47913,"Venezuela","Cabudare"],
    ["Monumental de Chile",47347,"Chile","Santiago"],
    ["Ciudad de Lanús",47027,"Argentina","Lanus"],
    ["Metropolitano de Barranquilla",46692,"Colombia","Barranquilla"],
    ["Olímpico Pascual Guerrero",46400,"Colombia","Cali"],
    ["General Pablo Rojas",45000,"Paraguay","Assunçao"],
    ["Atanasio Girardot",44739,"Colombia","Medellin"],
]


# INSERT INTO stadium_ownership VALUES(NULL, 6, 15);
# INSERT INTO stadium_ownership VALUES(NULL, 7, 15);
# INSERT INTO stadium_ownership VALUES(NULL, 14, 36);
# INSERT INTO stadium_ownership VALUES(NULL, 13, 17);
# INSERT INTO stadium_ownership VALUES(NULL, 61, 18);
# INSERT INTO stadium_ownership VALUES(NULL, 23, 19);
# INSERT INTO stadium_ownership VALUES(NULL, 9, 20);
# INSERT INTO stadium_ownership VALUES(NULL, 5, 29);
# INSERT INTO stadium_ownership VALUES(NULL, 4, 29);
# INSERT INTO stadium_ownership VALUES(NULL, 10, 33);
# INSERT INTO stadium_ownership VALUES(NULL, 67, 26);