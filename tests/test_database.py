import pytest
from src.db import Database


def test_database_add_and_get_data():
    db = Database(":memory:")  # Use in-memory database for testing
    game_board = {"board": "test_board"}
    
    game_struct = {"struct": "test_struct"}
    
    player_data = {"player1": "data1", "player2": "data2"}

    db.add_data(game_board, game_struct, player_data)
    data = db.get_data()

    assert len(data) == 1
    retrieved_game_board, retrieved_game_struct, retrieved_player_data = data[0]
    assert retrieved_game_board == {"board": "test_board"}
    assert retrieved_game_struct == {"struct": "test_struct"}
    assert retrieved_player_data == {"player1": "data1", "player2": "data2"}
