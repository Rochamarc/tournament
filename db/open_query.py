import os 

def change_directory(func):
    def wrapper(*args): 
        original_dir = os.getcwd()
        os.chdir(r'{}/db/query/'.format(os.getcwd()))
        
        s = func(args[0]) 
    
        os.chdir(original_dir)

        return s 
    return wrapper

class QueryHelper:
    
    @staticmethod
    @change_directory
    def open_create_query(query: str) -> str:
        ''' Prepare and return the string for the query '''
        s = None
        
        with open('create/create_{}'.format(query), 'r') as f:
            s = f.readlines()[0].replace('\n', '')
        
        return s

    @staticmethod
    @change_directory
    def open_insert_query(query: str) -> str: 
        ''' Prepare and return the string for the query '''
        s = None
        
        with open('insert/insert_{}'.format(query), 'r') as f:
            s = f.readlines()[0].replace('\n', '')

        return s
    
    @staticmethod
    @change_directory
    def open_update_query(query: str) -> str:
        ''' Prepare and return the string of the query '''
        s = None 

        with open('update/update+{}'.format(query), 'r') as f:
            s = f.readlines()[0].replace('\n', '')
        
        return s 

    @staticmethod 
    def create_query() -> None:
        ''' Creeate a query (migration) to the database '''
        pass 
