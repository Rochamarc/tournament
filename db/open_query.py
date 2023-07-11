import os 

class QueryHelper:
    @staticmethod
    def open_create_query(query: str) -> str:
        ''' Prepare and return the string for the query '''
        s = None
        
        original_dir = os.getcwd() # original directory
        os.chdir(r'{}/db/query/create/'.format(os.getcwd())) # change directory
        
        with open('create_{}'.format(query), 'r') as f:
            s = f.readlines()[0].replace('\n', '')

        os.chdir(original_dir) # gambiarra total

        return s

    @staticmethod 
    def create_query() -> None:
        ''' Creeate a query (migration) to the database '''
        pass 
