import os 

class QueryHelper:
    @staticmethod
    def open_create_query(query: str) -> str:
        ''' Prepare and return the string for the query '''
        s = None
        
        os.chdir(r'{}/db/query/create/'.format(os.getcwd())) # change directory
        
        with open('create_{}'.format(query), 'r') as f:
            s = f.readlines()[0].replace('\n', '')

        return s

    @staticmethod 
    def create_query() -> None:
        ''' Creeate a query (migration) to the database '''
        pass 
