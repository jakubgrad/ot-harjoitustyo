from database_connection import get_database_connection
from entities.house import Model


class ModelRepository():
    def __init__(self, connection):
        self._connection = connection

    def give_parameters(self)
        if not self.check_if_parameters_exist():
            print("Parameters don't exist")
            return False

        cursor = self._connection.cursor()
        #data = (username, password)
        print("Attempts to get parameters from db")

        cursor.execute('''
            SELECT (
                id, 
                year_min, 
                year_max,
                energy_consumption,
                pollution
            FROM
                house_age
        ''', data)

        result = cursor.fetchall()

        print(f"result of login query: {result}")

        #user_id = result['id']
        #username = result['username']
        #print("User object:")
        #print(f"user_user_id:{id},username:{username}")
        #user = User(user_id, username)
        if result:
            return True
        return False


    
model_repository = ModelRepository(get_database_connection(), model)
