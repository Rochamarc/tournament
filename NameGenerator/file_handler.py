def open_basic_files(dir_name: str, file_name: str) -> list[str]:
    ''' '''
    with open('./files/{}/{}.csv'.format(dir_name, file_name), 'r') as file:
        file = file.readlines()
        return [ name.replace('\n', '') for name in file ]

def open_language_files(dir_name: str, file_name: str) -> dict:
    ''' '''

    with open('./files/{}/{}.csv'.format(dir_name, file_name), 'r') as file:
        file = file.readlines()
        return [ name.replace('\n', '').split(',') for name in file ]
            

    
if __name__ == "__main__":
    print(open_language_files('first_names','asian_names'))
    