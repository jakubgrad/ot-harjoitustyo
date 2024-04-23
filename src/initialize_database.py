from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists houses;
    ''')

    cursor.execute('''
        drop table if exists administrators;
    ''')
    cursor.execute('''
        drop table if exists types_of_heating;
    ''')
    cursor.execute('''
        drop table if exists house_age;
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
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            parameters TEXT, 
            FOREIGN KEY(user_id) REFERENCES users(id)   
        );
    ''')

    cursor.execute('''
        CREATE TABLE administrators ( 
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE types_of_heating ( 
            id INTEGER PRIMARY KEY,
            type INTEGER,
            name TEXT,
            energy_consumption INTEGER,
            pollution INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE house_age ( 
            id INTEGER PRIMARY KEY,
            year_min INTEGER,
            year_max INTEGER,
            energy_consumption INTEGER,
            pollution INTEGER
        );
    ''')


    cursor.execute('''
        INSERT INTO administrators ( 
            username,
            password)
        VALUES (
            'm',
            'm'
        );
    ''')

    cursor.execute('''
        INSERT INTO house_age ( 
            year_min,
            year_max,
            energy_consumption,
            pollution )
        VALUES 
            (1900, 1989, 10, 10),
            (1990, 2000, 5, 7),
            (2001, 2010, 4, 6),  
            (2011, 2020, 3, 5),  
            (2021, 2030, 2, 4);  
    ''')

    cursor.execute('''
        INSERT INTO types_of_heating ( 
            type,
            name,
            energy_consumption,
            pollution )
        VALUES 
            (1, "Heat pump", 10, 10),
            (2, "Gas boiler", 8, 7),
            (3, "Electric heater", 12, 12),
            (4, "Wood stove", 6, 9),
            (5, "Solar panels", 3, 2),
            (6, "District heating", 9, 8),
            (7, "Oil boiler", 9, 10),
            (8, "Pellet stove", 7, 5),
            (9, "Geothermal heating", 5, 4);
    ''')



    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
