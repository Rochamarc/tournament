from random import choice

def generate_nationality(team_nationality):
    outsider_prob = choice([True, False, False, False, False, False])

    south = ['Brasil', 'Argentina', 'Uruguay', 'Ecuado', 'Peru', 'Chile', 'Venezuela', 'Paraguay', 'Bolivia', 'Guiana', 'Panama']
    

    if outsider_prob:
        # gringo
        return choice(south)
    
    return team_nationality

def generate_name(nationality):
    first_name_br = [
        'José', 'Antônio', 'José Antônio', 'Francisco', 'Carlos', 'Paulo', 'Pedro', 'Lucas', 'André', 'Luiz', 
        'Marcos', 'Gabriel', 'Luis', 'Matheus', 'Alvaro', 'Tales', 'Vinicius', 'Vanderlei', 'Vanderson', 'Wellington',
        'Junior', 'Aderson', 'Ademar', 'Bruno', 'Rafael', 'Daniel', 'Marcelo', 'Eduardo', 'Felipe', 'Philipe', 'Filipe',
        'Rodrigo', 'Davi', 'Miguel', 'Benjamin', 'Paulo Cezar', 'Joao Pedro', 'Joao Lucas', 'Joao Miguel', 'Gilmar', 'Gilvan',
        'Edvan', 'Renan', 'Rogerinho', 'Maurilio', 'Julinho', 'Juninho', 'Ronaldo', 'Theo', 'Samuel', 'Sandro', 'Luan', 'Patrick',
        'Pierre', 'Guilherme', 'Raizinho', 'Rodriguinho', 'Calebe', 'Lorenzo', 'Levi','Henrique', 'Ivan', 'Ian', 'Yago', 'Igor',
        'Leonardo', 'Leandro', 'Diogo', 'Diego', 'Dorival', 'Carlos Alberto', 'Manoel', 'Mariano', 'Marlon', 'Muriel', 'Wanderson'
    ]

    first_name_g = [
        'Juan', 'Gustavo', 'Benicio', 'Santiago', 'Angel', 'Javier', 'Lautaro', 'Paolo', 'Emiliano', 'Rodrigo', 'Leandro', 
        'Nicolás', 'Franco', 'Agustin', 'Lucas', 'Exequiel', 'Joaquin', 'Esteban', 'Guido', 'Nehuén', 'Giovani', 'Alfonso',
        'Diego', 'Miguel', 'Christian', 'Rocco', 'Patricio', 'Enrique', 'Teodoro', 'Tomás', 'Eugenio', 'Enzo', 'Hermán', 'Hernán',
        'Frederico', 'Alberto', 'Iván', 'Aldo', 'Jorge', 'José', 'Rafael', 'Guillermo', 'Yamir', 'Brayan', 'Piero', 'Estefano', 'Rafael',
        'Héctor', 'Frederico','Fabián', 'Maxi'
    ]

    last_names_g = [
        'Quintero', 'del Toro', 'De La Cruz', 'di Maria', 'Armani', 'Martinez', 'Borré', 'Palavecino', 'Maidana', 'Paredes', 'Fontana',
        'Suarez', 'Diaz', 'Rojas', 'Rojo', 'Bologna', 'Castro', 'Maduro', 'Álvarez', 'Pavón', 'del Riego', 'Zárate', 'Villa', 'Cuellar',
        'Gomez', 'Izquierdo', 'Soldano', 'López', 'Vázquez', 'Gonzalez', 'Zeballos', 'Calpado', 'Giampaolli', 'Sampaoli', 'Jara',
        'Viña', 'Cuesta', 'Cueva', 'Sanchez', 'Ortiz', 'Faravelli', 'Montenegro', 'Hurtado', 'Pellerano', 'Chávez', 'Plaza', 'Murillo', 'Pinos',
        'Arroyo', 'Guerrero', 'Mari', 'Isla', 'de Arrascaeta', 'Caicedo', 'Cañete', 'Aránguiz', 'Arias', 'Luján', 'Hernandez', 'dos Santos', 'De La Muerte'
    ]

    last_names_br = [
        'Rocha', 'Santos', 'Silva', 'Mota', 'Dias', 'Ribeiro', 'Monteiro', 'Melila', 'Licurgo', 'Souza', 'Grilo',
        'Melo', 'Barbosa', 'Lopes', 'Pereira', 'Veron', 'Coutinho', 'Lima', 'Falcao', 'Menezes', 'Mendes', 'Silvestre', 
        'Brandão', 'Padrão', 'Varanda', 'Magno', 'da Costa', 'da Silva', 'de Paula', 'Cunha', 'Garcia', 'Oliveira', 'Martinelli', 
        'Cazares', 'Becker', 'Carvalho', 'Claro', 'Barata', 'Calegari', 'Fernandes', 'Borges', 'Brito', 'Araujo', 'Barcelos','Teixeira',
        'Pacheco', 'Teles', 'Neres', 'Militão', 'Nascimento', 'Frazan', 'Faria', 'Nogueira', 'de Castro', 'Arantes', 'Arouca', 'Ribas', 'Pereira', 'Viana',
        'Dos Anjos', 'Muniz', 'Azevedo', 'Rios', 'Cruz', 'Barreto', 'Paes', 'Rosa'
    ]

    if nationality == 'Brasil':
        return f"{choice(first_name_br)} {choice(last_names_br)}"
    return f"{choice(first_name_g)} {choice(last_names_g)}"