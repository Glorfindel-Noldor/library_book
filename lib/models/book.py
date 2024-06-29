from models.__init__ import CONNECTION, CURSOR



class book:
    def __init__ (self, name, id_ = None):
        self.name = name
        self.id = id_
        self.foreign_id = None
    
    @classmethod
    def drop_table(cls):
        '''Drop the Book table for clearing purposes'''
        sql = "DROP TABLE IF EXISTS books;"
        CURSOR.execute(sql)
        CONNECTION.commit()

