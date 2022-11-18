import sqlite3 # https://youtu.be/lFRMdGfo_XA

class GameDB:
    
    def __init__(self):
        pass
    
    def data_connection(self, name_db):
        self.connection = sqlite3.connect("game.db")
    
    def create_table(self, table_name, **kargs):
        pass
