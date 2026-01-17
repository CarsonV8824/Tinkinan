import pytest
from src.db import Database

def test_database_add_and_get_data():
    with Database("database/Test_Tinkinan.db") as db:
        db.clear_data()
        
        game_struct_data = {"game_struct": "test_game_struct"}
        player_data = {"player": "test_player"}
        db.add_data(game_struct_data, player_data)
        data = db.get_data()
        assert len(data) == 1
        assert type(data[0][0]) == int
        assert data[0][1] == game_struct_data
        assert data[0][2] == player_data

def test_database_clear_data():
    with Database("database/Test_Tinkinan.db") as db:
        db.clear_data()
        game_struct_data = {"game_struct": "test_game_struct"}
        player_data = {"player": "test_player"}
        db.add_data(game_struct_data, player_data)
        db.clear_data()
        data = db.get_data()
        assert len(data) == 0
        db.add_data(game_struct_data, player_data)
        db.clear_data()
        data = db.get_data()

        assert len(data) == 0



