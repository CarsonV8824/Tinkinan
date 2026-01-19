from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk

from tabs import Tabs
from canvas import Canvas
from game_struct import GameStruct
from db import Database
from game_struct import GameStruct
from game_loop import GameLoop
from player import Player
import networkx as nx
import random

def load_data():
    try:
        with Database("database/Tinkinan.db") as db:
            data = db.get_data()
            if not data:
                return None
        return data
    except Exception as e:
        print (e)

def add_data(game_struct:GameStruct, PlayerData:list[Player]):
    try:
        with Database("database/Tinkinan.db") as db:
            node_list = list(game_struct.graph.nodes(data=True))
            edge_list = list(game_struct.graph.edges(data=True))
            
            player_data = []
            for player in PlayerData:
                pdata = {
                    "name": player.name,
                    "color": player.color,
                    "resources": player.resources,
                    "settlements": player.settlements,
                    "cities": player.cities,
                    "roads": player.roads
                }
                player_data.append(pdata)
                
            db.add_data(node_list, edge_list, player_data)
    except Exception as e:
        print (e)

def main():
    
    root = ThemedTk(theme="breeze")
    root.geometry("1200x800")
    root.title("Catan in Tkinter")

    root.iconbitmap("src/hexagon.ico")

    game_struct = GameStruct()
    
    board = Canvas(root, game_struct)

    game_loop = GameLoop(root, game_struct, board)

    player_count = game_loop.start_screen()

    players = []
    
    colors = ["red", "blue", "purple", "orange"]
    
    for i in range(player_count):
        
        players.append(Player(f"Player {i+1}", colors[i]))

    tab = Tabs(root)

    tabs = tab.tabs()

    game_loop.placing_initial_settlements(players, tabs=tabs)

    first_player_index  = 0

    board.get_player(players[first_player_index]) #set first player for placement

    dice_tab = tab.dice_tab(tabs, game_loop, players)

    player_stats_tab = tab.player_stats_tab(tabs, players)

    tab.update_player_stats(players) 

    trade_tab = tab.trade_tab(tabs, players, game_loop, game_struct)

    buy_tab = tab.buy_tab(tabs, players, game_loop)
    
    rules_tab = tab.rules_tab(tabs)

    past_games_tab = tab.past_games_tab(tabs, load_data())
    
    running = root.mainloop()

    if not running: #this will run when the window is closed
        print("Exiting Game")
        
        add_data(game_struct, players)

if __name__ == "__main__":
    main()