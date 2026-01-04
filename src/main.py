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
import random

def load_data():
    try:
        with Database("database/Catan.db") as db:
            data = db.get_data()
            if not data:
                return None
        return data
    except Exception as e:
        print (e)

def main():
    
    root = ThemedTk(theme="breeze")
    root.geometry("1200x800")
    root.title("Catan in Tkinter")

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

    dice_tab = tab.dice_tab(tabs, game_loop, players)

    player_stats_tab = tab.player_stats_tab(tabs, players)

    tab.update_player_stats(players) 

    trade_tab = tab.trade_tab(tabs)

    biuld_tab = tab.biuld_tab(tabs)

    rules_tab = tab.rules_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()