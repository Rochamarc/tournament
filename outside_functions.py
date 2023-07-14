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
