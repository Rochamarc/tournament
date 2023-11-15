-- Campeonato Brasileiro
INSERT INTO competitions VALUES(NULL, 'Campeonato Brasileiro');

-- Liga Profesional de Fútbol
INSERT INTO competitions VALUES(NULL, 'Liga Profesional de Futbol');


-- CUPS 
INSERT INTO competitions VALUES(NULL, 'Copa do Brasil');
INSERT INTO competitions VALUES(NULL, 'Copa Libertadores da America');

-- Brasilian divisions
INSERT INTO divisions VALUES(NULL, 'Serie A', 1);
INSERT INTO divisions VALUES(NULL, 'Serie B', 1);
INSERT INTO divisions VALUES(NULL, 'Serie C', 1);

-- Argentinian first division
INSERT INTO divisions VALUES(NULL, 'Primera Divison', 2);

/* INSERT SERIE A CLUBS OF 2022 SEASON */

INSERT INTO clubs VALUES(NULL, 'América Mineiro', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Atlético Mineiro', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Athletico Paranaense', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Ceará', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Fortaleza', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Flamengo', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Fluminense', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Cuiabá', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Grêmio', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'International', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Chapecoense', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Juventude', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'São Paulo', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Corinthians', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Palmeiras', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Santos', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Red Bull Bragantino', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Sport Recife', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Bahia', 'Brazil');
INSERT INTO clubs VALUES(NULL, 'Atlético Goianiense', 'Brazil');

/* INSERTING CLUBS OF THE FIRST division FROM THE BRAZILLAN CHAMPIONSHIP */

INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 1, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 2, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 3, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 4, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 5, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 6, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 7, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 8, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 9, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 10, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 11, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 12, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 13, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 14, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 15, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 16, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 17, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 18, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 19, 1);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 20, 1);

/* SECOND division */

INSERT INTO clubs VALUES(NULL, "Vasco da Gama", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Botafogo", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Cruzeiro", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Operário", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Coritiba", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Goiás", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Guarani", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Avaí", 'Brazil');
INSERT INTO clubs VALUES(NULL, "CRB", 'Brazil');
INSERT INTO clubs VALUES(NULL, "CSA", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Náutico", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Sampaio Corrêa", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Vila Nova", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Ponte Preta", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Brusque", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Remo", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Londrina", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Vitória", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Confiança", 'Brazil');
INSERT INTO clubs VALUES(NULL, "Brasil de Pelotas", 'Brazil');

INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 21, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 22, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 23, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 24, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 25, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 26, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 27, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 28, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 29, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 30, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 31, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 32, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 33, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 34, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 35, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 36, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 37, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 38, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 39, 2);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 40, 2);

/* THIRD division*/

INSERT INTO clubs VALUES(NULL, "Paysandu", "Brazil");
INSERT INTO clubs VALUES(NULL, "Tombense", "Brazil");
INSERT INTO clubs VALUES(NULL, "Botafogo-PB", "Brazil");
INSERT INTO clubs VALUES(NULL, "Manaus", "Brazil");
INSERT INTO clubs VALUES(NULL, "Volta Redonda", "Brazil");
INSERT INTO clubs VALUES(NULL, "Ferroviário", "Brazil");
INSERT INTO clubs VALUES(NULL, "Altos", "Brazil");
INSERT INTO clubs VALUES(NULL, "Floresta", "Brazil");
INSERT INTO clubs VALUES(NULL, "Jacuipense", "Brazil");
INSERT INTO clubs VALUES(NULL, "Santa Cruz", "Brazil");
INSERT INTO clubs VALUES(NULL, "Novorizontino", "Brazil");
INSERT INTO clubs VALUES(NULL, "Ituano", "Brazil");
INSERT INTO clubs VALUES(NULL, "Ypiranga", "Brazil");
INSERT INTO clubs VALUES(NULL, "Criciúma", "Brazil");
INSERT INTO clubs VALUES(NULL, "Figueirense", "Brazil");
INSERT INTO clubs VALUES(NULL, "São José", "Brazil");
INSERT INTO clubs VALUES(NULL, "Botafogo SP", "Brazil");
INSERT INTO clubs VALUES(NULL, "Mirasol", "Brazil");
INSERT INTO clubs VALUES(NULL, "Paraná", "Brazil");
INSERT INTO clubs VALUES(NULL, "Oeste", "Brazil");

INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 41, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 42, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 43, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 44, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 45, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 46, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 47, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 48, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 49, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 50, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 51, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 52, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 53, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 54, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 55, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 56, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 57, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 58, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 59, 3);
INSERT INTO championships (season, club_id, division_id ) VALUES ('2022', 60, 3);

/* ARGENTINIAN CHAMPIONSHIPS */

INSERT INTO clubs VALUES(NULL, "River Plate", "Argentina");
INSERT INTO clubs VALUES(NULL, "Talleres (Córdoba)", "Argentina");
INSERT INTO clubs VALUES(NULL, "San Lorenzo", "Argentina");
INSERT INTO clubs VALUES(NULL, "Lanús", "Argentina");
INSERT INTO clubs VALUES(NULL, "Estudiantes de La Plata", "Argentina");
INSERT INTO clubs VALUES(NULL, "Defensa y Justicia", "Argentina");
INSERT INTO clubs VALUES(NULL, "Boca Juniors", "Argentina");
INSERT INTO clubs VALUES(NULL, "Rosário Central", "Argentina");
INSERT INTO clubs VALUES(NULL, "Godoy Cruz Antonio Tomba", "Argentina");
INSERT INTO clubs VALUES(NULL, "Argentinos Juniors", "Argentina");
INSERT INTO clubs VALUES(NULL, "Atlético Tucumán", "Argentina");
INSERT INTO clubs VALUES(NULL, "Racing Club", "Argentina");
INSERT INTO clubs VALUES(NULL, "Belgrano (Córdoba)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Newell's Old Boys", "Argentina");
INSERT INTO clubs VALUES(NULL, "Barracas Central", "Argentina");
INSERT INTO clubs VALUES(NULL, "Tigre", "Argentina");
INSERT INTO clubs VALUES(NULL, "Platense", "Argentina");
INSERT INTO clubs VALUES(NULL, "Instituto (Córdoba)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Sarmiento (Junín)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Unión (Santa Fe)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Banfield", "Argentina");
INSERT INTO clubs VALUES(NULL, "Gimnasia La Plata", "Argentina");
INSERT INTO clubs VALUES(NULL, "Central Córdoba (Santiago del Estero)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Independiente", "Argentina");
INSERT INTO clubs VALUES(NULL, "Vélez Sarsfield", "Argentina");
INSERT INTO clubs VALUES(NULL, "Huracán", "Argentina");
INSERT INTO clubs VALUES(NULL, "Colón (Santa Fe)", "Argentina");
INSERT INTO clubs VALUES(NULL, "Arsenal Sarandi", "Argentina");

INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 61, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 62, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 63, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 64, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 65, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 66, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 67, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 68, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 69, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 70, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 71, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 72, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 73, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 74, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 75, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 76, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 77, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 78, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 79, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 80, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 81, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 82, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 83, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 84, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 85, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 86, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 87, 4);
INSERT INTO championships(season, club_id, division_id) VALUES ('2022', 88, 4);


/* GENERIC STADIUMS */

INSERT INTO stadiums(name, capacity, country) VALUES('Rei Pelé Arena', 100000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Estádio Porto Alegre', 65000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Estádio Arthur Antunes Coimbra', 70000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena do Castelo', 90000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena Dom Pedro II', 150000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Estádio do Tupiniquim', 30000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Zumbi dos Palmares', 30000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena Princesa Izabel', 62000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena Joviedade', 200000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Estádio da Paulista', 150000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Estádio Sertanejo', 120000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena Mário Jorge Lobo Zagallo', 70000 ,'Brazil');
INSERT INTO stadiums(name, capacity, country) VALUES('Arena João Leite Ortiz', 35000 ,'Brazil');

/* REAL STADIUMS */

INSERT INTO stadiums(name, capacity, country, city) VALUES("Monumental de la U",80903,"Peru","Lima");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Maracanã",78838,"Brazil","Rio de Janeiro");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Mané Garrincha",72788,"Brazil","Brasília");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Morumbi",72039,"Brazil","Sao Paulo");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Monumental de Núñez",70074,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Mineirão",61846,"Brazil","Belo Horizonte");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Arena do Grêmio",60540,"Brazil","Porto Alegre");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Centenario",60235,"Uruguay","Montevideu");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Estadio Nacional del Peru",60000,"Peru","Lima");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Arruda",60044,"Brazil","Recife");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Estadio Monumental Isidro Romero Carbo",57267,"Ecuador","Guayaquil");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Estadio Mario Alberto Kempes",57000,"Argentina","Cordoba");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Estadio La Bombonera",54000,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Municipal João Avelange",53350,"Brazil","Uberlandia");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Ciudad de La Plata",53000,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Castelão",52552,"Brazil","Fortaleza");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Deportivo Cali",52000,"Colombia","Cali");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Monumental de Maturín",51796,"Venezuela","Maturin");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Presidente Juan Domingo Perón",51389,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Beira-Rio",50842,"Brazil","Porto Alegre");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Libertadores da America",49592,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("José Amalfitani",49540,"Argentina","Buenos Aires");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Néo Química Arena",49205,"Brazil","Sao Paulo");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Nacional de Chile",48665,"Chile","Santiago");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Metropolitano Lara",47913,"Venezuela","Cabudare");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Monumental de Chile",47347,"Chile","Santiago");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Ciudad de Lanús",47027,"Argentina","Lanus");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Metropolitano de Barranquilla",46692,"Colombia","Barranquilla");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Olímpico Pascual Guerrero",46400,"Colombia","Cali");
INSERT INTO stadiums(name, capacity, country, city) VALUES("General Pablo Rojas",45000,"Paraguay","Assunçao");
INSERT INTO stadiums(name, capacity, country, city) VALUES("Atanasio Girardot",44739,"Colombia","Medellin");

/* Stadium ownership */

-- Maracana
INSERT INTO stadium_ownership VALUES(NULL, 6, 15);
INSERT INTO stadium_ownership VALUES(NULL, 7, 15);

-- Neo quimica
INSERT INTO stadium_ownership VALUES(NULL, 14, 36);

-- morumbi
INSERT INTO stadium_ownership VALUES(NULL, 13, 17);

-- monumental
INSERT INTO stadium_ownership VALUES(NULL, 61, 18);

-- Mineirao
INSERT INTO stadium_ownership VALUES(NULL, 23, 19);

-- Arena gremio
INSERT INTO stadium_ownership VALUES(NULL, 9, 20);

-- castelao
INSERT INTO stadium_ownership VALUES(NULL, 5, 29);
INSERT INTO stadium_ownership VALUES(NULL, 4, 29);

-- beira rio
INSERT INTO stadium_ownership VALUES(NULL, 10, 33);

-- Bombonera
INSERT INTO stadium_ownership VALUES(NULL, 67, 26);