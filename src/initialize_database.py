from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists houses;
    ''')


    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE houses ( 
            id INTEGER, 
            user_id INTEGER,
            parameters TEXT, 
            FOREIGN KEY(user_id) REFERENCES users(id)   
        );
    ''')
    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
