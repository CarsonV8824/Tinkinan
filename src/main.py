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

    first_dice = ttk.Label(root, text="First Dice Roll: ")
    first_dice.pack()

    second_dice = ttk.Label(root, text="Second Dice Roll: ")
    second_dice.pack()

    total_of_dies = ttk.Label(root, text="Total of Dice: ")
    total_of_dies.pack()

    game_struct = GameStruct()
    
    board = Canvas(root, game_struct)

    game_loop = GameLoop(root, game_struct, board, first_dice, second_dice, total_of_dies)

    player_count = game_loop.start_screen()

    players = []
    
    colors = ["red", "blue", "green", "yellow"]
    
    for i in range(player_count):
        
        players.append(Player(f"Player {i+1}", colors[i]))

    first_settlements = game_loop.place_initial_settlements(players)

    tab = Tabs(root)

    tabs = tab.tabs()
    
    dice_tab = tab.dice_tab(tabs, game_loop, players)

    player_stats_tab = tab.player_stats_tab(tabs, players)

    tab.update_player_stats(players) 

    trade_tab = tab.trade_tab(tabs)

    biuld_tab = tab.biuld_tab(tabs)

    rules_tab = tab.rules_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()