class BaseController:
    @classmethod
    def get_select_query(cls, file_name: str) -> str:
        ''' Return a string query by a file in sql '''
        file_path = 'db/queries/select/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
    
    @classmethod
    def get_update_query(cls, file_name: str) -> str:
        ''' Retuarn a string query '''
        file_path = 'db/queries/update/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except:
            raise FileNotFoundError("File {} doesn't exists".format(file_path))

    @classmethod
    def get_insert_query(cls, file_name: str) -> str:
        ''' Return a string query by a file in sql '''
        file_path = 'db/queries/insert/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except:
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
        
    @classmethod
    @property
    def database_config(cls):
        return { 
            'user': 'tournament_user', 
            'host': 'localhost', 
            'password': 'tournament_pass', 
            'database': 'tournament' 
        }