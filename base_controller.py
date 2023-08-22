class BaseController:
    @classmethod
    def get_query(cls, file_name: str) -> str:
        ''' Return a string query by a file in sql '''
        try:
            with open('queries/select/{}.sql'.format(file_name), 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File name doesn't exists")
    
    @classmethod
    @property
    def database_config(cls):
        return { 'user': 'tournament_user', 'host': 'localhost', 'password': 'tournament_pass', 'database': 'football' }