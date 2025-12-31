import sqlite3
import json

class Database:

    def __init__(self, file="database/db/Catan.db"):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.__make_table()

    def __make_table(self):
        self.cursor.execute(
        """CREATE TABLE IF NOT EXISTS Catan (
        GameBoard TEXT,
        PlayerData Text
        );""")
        self.connection.commit()

    def add_data(self, GameBoard, PlayerData):
        self.cursor.execute("""
        INSERT INTO Catan (GameBoard, PlayerData)
        Values (?, ?)
    
        """, (json.dumps(GameBoard), json.dumps(PlayerData),))
        self.connection.commit()

    def get_data(self):
        self.cursor.execute("""SELECT * FROM Catan""")
        data = self.cursor.fetchall()
        return [ (json.loads(row[0]), json.loads(row[1])) for row in data ]
    
    def clear_data(self):
        self.cursor.execute("""DELETE FROM Catan""")
        self.connection.commit()

    def __del__(self):
        self.connection.close()
    

