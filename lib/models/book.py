from models.__init__ import CONNECTION, CURSOR

class Book:
    def __init__(self, name, foreign_id=None, id_=None):
        self.name = name
        self.foreign_id = foreign_id or self.get_default_id()
        self.id = id_

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books;"
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            foreign_id INTEGER,
            FOREIGN KEY (foreign_id) REFERENCES libraries(id)
        );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    def save(self):
        sql = "INSERT INTO books (name, foreign_id) VALUES (?, ?);"
        CURSOR.execute(sql, (self.name, self.foreign_id))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @staticmethod
    def get_default_id():
        sql = "SELECT id FROM libraries LIMIT 1;"
        CURSOR.execute(sql)
        id_ = CURSOR.fetchone()
        return id_[0] if id_ else None

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books;"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM books WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone()

    @classmethod
    def delete_book(cls, id):
        sql = "DELETE FROM books WHERE id = ?;"
        CURSOR.execute(sql, (id,))
        CONNECTION.commit()

