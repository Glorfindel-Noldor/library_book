from models.__init__ import CONNECTION, CURSOR

class Library:
    all_objs = {}

    def __init__(self, name, id_=None):
        self.name = name
        self.id = id_
        type(self).all_objs[self.id] = self

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
        cls.all_objs.pop(id, None)

    def save(self):
        if self.id is None:
            sql = "INSERT INTO libraries (name) VALUES (?);"
            CURSOR.execute(sql, (self.name,))
            CONNECTION.commit()
            self.id = CURSOR.lastrowid
            type(self).all_objs[self.id] = self
        else:
            sql = "UPDATE libraries SET name = ? WHERE id = ?;"
            CURSOR.execute(sql, (self.name, self.id))
            CONNECTION.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM libraries;"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def all_lib_id(cls):
        sql = "SELECT id FROM libraries;"
        CURSOR.execute(sql)
        return [row[0] for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM libraries WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(name=row[1], id_=row[0])
        return None

    def get_books(self):
        sql = """
        SELECT books.id, books.name 
        FROM books 
        JOIN libraries ON books.foreign_id = libraries.id 
        WHERE libraries.id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()
