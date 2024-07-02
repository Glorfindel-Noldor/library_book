from models.__init__ import CONNECTION, CURSOR

class Library:
    def __init__(self, name, id_=None):
        self.name = name
        self.id = id_

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS libraries;"
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_library_table(cls):
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
        sql = "DELETE FROM libraries WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        CONNECTION.commit()

    def save(self):
        sql = "INSERT INTO libraries (name) VALUES (?);"
        CURSOR.execute(sql, (self.name,))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM libraries;"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM libraries WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone()

    def get_books(self):
        sql = "SELECT * FROM books WHERE foreign_id = ?;"
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()