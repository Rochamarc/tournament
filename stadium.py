from classes import Stadium

""" name: 'Maracanã', 'capacity': 78 838, 'location': 'Rio de Janeiro, Brasil , 'club_owner': None """

# Missing
# Serra Dourada, Fonte Nova, Tomás Adolfo Ducó, Pedro Bidegain, Engenhão, Allianz Parque
# Malvinas Argentinas, Arena da Baixada, Defensores del Chaco, Metropolitano de Mérida, Garcilaso de la Vega 

stadiums = [
    { "name": "Monumental de la U", "capacity": 80_903, "location": 'Lima, Peru', "club_owner": 'Universitario de Deportes' },
    { "name": "Maracanã", "capacity": 78_838, "location": 'Rio de Janeiro, Brasil', "club_owner": 'Flamengo/Fluminense' },
    { "name": "Mané Garrincha", "capacity": 72_788, "location": 'Brasília, Brasil', "club_owner": None },
    { "name": "Morumbi", "capacity": 72_039, "location": 'São Paulo, Brasil', "club_owner": 'São Paulo' },
    { "name": "Monumental de Núñez", "capacity": 70_074, "location": 'Buenos Aires, Argentina', "club_owner": 'River Plate' },
    { "name": "Mineirão", "capacity": 61_846, "location": 'Belo Horizonte, Brasil', "club_owner": 'Cruzeiro/Atlético Mineiro' },
    { "name": "Arena do Grêmio", "capacity": 60_540, "location": 'Porto Alegre, Brasil', "club_owner": 'Grêmio' },
    { "name": "Centenario", "capacity": 60_235, "location": 'Monetevidéu, Uruguay', "club_owner": 'Nacional/Peñarol' },
    { "name": "Estadio Nacional del Peru", "capacity": 60_000, "location": 'Lima, Peru', "club_owner": None },
    { "name": "Arruda", "capacity": 60_044, "location": 'Recife, Brasil', "club_owner": 'Santa Cruz' },
    { "name": "Estadio Monumental Isidro Romero Carbo", "capacity": 57_267, "location": 'Guayaquil, Ecuador', "club_owner": 'Barcelona de Guayaquil' },
    { "name": "Estadio Mario Alberto Kempes", "capacity": 57_000, "location": 'Córdoba, Argentina', "club_owner": 'Talleres/Belgrano/Instituto' },
    { "name": "Estadio La Bombonera", "capacity": 54_000, "location": 'Buenos Aires, Argentina', "club_owner": 'Boca Juniors' },
    { "name": "Municipal João Avelange", "capacity": 53_350, "location": 'Uberlândia, Brasil', "club_owner": 'Uberlândia' },
    { "name": "Ciudad de La Plata", "capacity": 53_000, "location": 'Buenos Aires', "club_owner": 'Estudiantes/Gimnasia y Esgrima' },
    { "name": "Castelão", "capacity": 52_552, "location": 'Fortaleza, Brasil', "club_owner": 'Ceará/Fortaleza' },
    { "name": "Deportivo Cali", "capacity": 52_000, "location": 'Cali, Colombia', "club_owner": 'Deportivo Cali' },
    { "name": "Monumental de Maturín", "capacity": 51_796, "location": 'Maturín, Venezuela', "club_owner": 'Monagas' },
    { "name": "Presidente Juan Domingo Perón", "capacity": 51_389, "location": 'Buenos Aires, Argentina', "club_owner": 'Racing' },
    { "name": "Beira-Rio", "capacity": 50_842, "location": 'Porto Alegre, Brasil', "club_owner": 'Internacional' },
    { "name": "Libertadores da America", "capacity": 49_592, "location": 'Buenos Aires, Argentina', "club_owner": 'Independiente' },
    { "name": "José Amalfitani", "capacity": 49_540, "location": 'Buenos Aires, Argentina', "club_owner": 'Vélez Sársfield' },
    { "name": "Néo Química Arena", "capacity": 49_205, "location": 'São Paulo, Brasil', "club_owner": 'Corinthians  ' },
    { "name": "Nacional de Chile", "capacity": 48_665, "location": 'Santiago, Chile', "club_owner": 'Universidad de Chile' },
    { "name": "Metropolitano Lara", "capacity": 47_913, "location": 'Cabudare, Venezuela', "club_owner": 'Deportivo Lara' },
    { "name": "Monumental de Chile", "capacity": 47_347, "location": 'Santiago, Chile', "club_owner": 'Colo-Colo' },
    { "name": "Ciudad de Lanús", "capacity": 47_027, "location": 'Lanús, Argentina', "club_owner": 'Lánus' },
    { "name": "Metropolitano de Barranquilla", "capacity": 46_692, "location": 'Barranquilla, Colombia', "club_owner": 'Junior' },  	 	
    { "name": "Olímpico Pascual Guerrero", "capacity": 46_400, "location": 'Cali, Colombia', "club_owner": 'América de Cali' },
    { "name": "General Pablo Rojas", "capacity": 45_000, "location": 'Assunção, Paraguay', "club_owner": 'Cerro Porteño' },
    { "name":  "Atanasio Girardot", "capacity": 44_739, "location": 'Medellín, Colombia', "club_owner": 'Atlético Nacional/Independiente Medellín' }
]

print("Inserindo estadios na base de dados!")
for i in stadiums:
    Stadium(i["name"], i["location"], capacity=i['capacity'], club_owner=i['club_owner']).db_insertion()
print("Estadio inseridos com sucesso!")