import sqlite3
import json
import pickle

class Database:

    def __init__(self, file="database/Tinkinan.db"):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.__make_table()

    def __make_table(self):
        self.cursor.execute(
        """CREATE TABLE IF NOT EXISTS Catan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        GameStruct BLOB,
        PlayerData BLOB
        );""")
        self.connection.commit()

    def add_data(self, GameStruct, PlayerData):
        self.cursor.execute("""
        INSERT INTO Catan (GameStruct, PlayerData)
        Values (?, ?)
    
        """, (pickle.dumps(GameStruct), pickle.dumps(PlayerData)))
        self.connection.commit()

    def get_data(self):
        self.cursor.execute("""SELECT * FROM Catan""")
        data = self.cursor.fetchall()
        return [ (row[0], pickle.loads(row[1]), pickle.loads(row[2])) for row in data ]
    
    def clear_data(self):
        self.cursor.execute("""DELETE FROM Catan""")
        self.connection.commit()

    def __del__(self):
        self.connection.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

