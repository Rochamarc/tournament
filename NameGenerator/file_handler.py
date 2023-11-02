def open_basic_files(dir_name: str, file_name: str) -> list[str]:
    """Open files that only has on item by row 
    in NameGenerator/files/{dir_name}/{file_name}.csv

    Parameters
    ----------
    dir_name : str
        String with the directory name inside files
    file_name : str
        Name of the file without the extension

    Returns
    -------
        A list of lists with names
    """
    
    with open('./files/{}/{}.csv'.format(dir_name, file_name), 'r') as file:
        file = file.readlines()
        return [ name.replace('\n', '') for name in file ]

def open_language_files(dir_name: str, file_name: str) -> dict:
    """Open files that has two items by row 
    in NameGenerator/files/{dir_name}/{file_name}.csv

    Parameters
    ----------
    dir_name : str
        String with the directory name inside files
    file_name : str
        Name of the file without the extension

    Returns
    -------
        A list of lists with names
    """

    with open('./files/{}/{}.csv'.format(dir_name, file_name), 'r') as file:
        file = file.readlines()
        return [ name.replace('\n', '').split(',') for name in file ]
            

    
if __name__ == "__main__":
    print(open_language_files('first_names','asian_names'))
    