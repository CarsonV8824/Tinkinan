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
        db = Database()
        return db.get_data()
    except Exception as e:
        print (e)

def main():
    
    root = ThemedTk(theme="breeze")
    root.geometry("1200x800")
    root.title("Catan in Tkinter")

    game_struct = GameStruct()
    
    board = Canvas(root, game_struct)

    player_count = GameLoop(root, game_struct, board).start_screen()

    players = []
    
    colors = ["red", "blue", "green", "yellow"]
    
    for i in range(player_count):
        
        players.append(Player(f"Player {i+1}", colors[random.randint(0, len(colors)-1)]))

    tab = Tabs(root)

    tabs = tab.tabs()

    dice_tab = tab.dice_tab(tabs)

    player_stats_tab = tab.player_stats_tab(tabs, players)

    tab.update_player_stats(players) #use this to update player stats later

    trade_tab = tab.trade_tab(tabs)

    biuld_tab = tab.biuld_tab(tabs)

    rules_tab = tab.rules_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()