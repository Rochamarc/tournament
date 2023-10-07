import mysql.connector
from db.base_controller import BaseController

class StadiumsController(BaseController):
    @classmethod
    def select_all_stadiums(cls) -> list[set]:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_stadiums'))

        stadiums = cursor.fetchall()

        conn.close()
        return stadiums 