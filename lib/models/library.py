from models.__init__ import CONNECTION, CURSOR

class Library:
    def __init__(self, name, id_=None):
        self.name = name
        self.id = id_    

    @classmethod
    def drop_table(cls):
        '''Drop the Library table for clearing purposes'''
        sql = "DROP TABLE IF EXISTS library;"
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_library_table(cls):
        '''Create the Library table'''
        sql = """
        CREATE TABLE IF NOT EXISTS libraries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def delete_library(cls, id):
        '''Delete a library by id'''
        sql = "DELETE FROM libraries WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        CONNECTION.commit()

    def save(self):
        '''Save a library to the database'''
        sql = "INSERT INTO libraries (name) VALUES (?);"
        CURSOR.execute(sql, (self.name,))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        '''Get all libraries from the database'''
        sql = "SELECT * FROM libraries;"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
