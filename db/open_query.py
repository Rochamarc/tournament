class QueryHelper:
    @staticmethod
    def open_create_query(query: str) -> str:
        ''' Prepare and return the string for the query '''
        s = None
        with open(f'query/create/create_{query}', 'r') as f:
            s = f.readlines()[0].replace('\n', '')

        return s

    @staticmethod 
    def create_query() -> None:
        ''' Creeate a query (migration) to the database '''
        pass 
