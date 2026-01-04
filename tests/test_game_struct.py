import pytest
from src.game_struct import GameStruct
from src.player import Player

def test_add_player_to_house():
    game_struct = GameStruct()
    corner_num = 1
    player_name = "Player 1"
    house_type = "House"

    game_struct.add_player_to_house(corner_num, player_name, house_type)

    node = game_struct.graph.nodes[f"House{corner_num}"]
    assert node["Player"] == player_name
    assert node["Type"] == house_type