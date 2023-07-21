def open_file(text_file_name: str) -> None:
    ''' Print a file on files/basic files '''
    with open(f'files/basic_files/{text_file_name}.txt', 'r') as f:
        for line in f.readlines():
            if line != '\n': print(line.replace('\n',''))
    
    return None

def filter_line(line:str) -> str:
    ''' Threat a line removing useless chars '''
    
    line = line.split(',') 
    line[-1] = line[-1].replace('\n', '')
    return line 

def filter_line_for_club(line: str) -> dict:
    ''' Receive a line from a club file and convert the line into data file '''
    line = line.split(',')
    name = line[0] 
    state = line[1].replace('\n', '') 
    club_class = line[-1].replace('\n', '')
    return { 'name': name, 'state': state, 'club_class': club_class}

def filter_line_for_stadium(line:str, has_club_owner=False) -> dict:
    ''' Receive a line from a stadium file and convert the line into data file '''
    line = line.split(',')
    name = line[0]
    capacity = line[1]
    city = line[2]
    country = line[3]
    location = f'{city}, {country}'
    club_owner = line[-1].replace('\n', '') if has_club_owner else None

    return { 'name': name, 'capacity': capacity, 'location': location, 'club_owner': club_owner }
