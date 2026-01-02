from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
import random
from game_struct import GameStruct
from canvas import Canvas



class GameLoop:
    
    def __init__(self, root: tk.Tk, game_struct: GameStruct, board: Canvas, first_dice:ttk.Label=None, second_dice:ttk.Label=None, total_of_dice:ttk.Label=None):
        
        self.root = root
        self.game_struct = game_struct
        self.board = board
        self.player_count = 3
        self.first_dice = first_dice
        self.second_dice = second_dice
        self.total_of_dice = total_of_dice

    def start_screen(self):
        self.root.withdraw()  
        
        self.first_screen = tk.Toplevel(self.root)
        self.first_screen.geometry("400x300")
        self.first_screen.title("Welcome to Catan")
        
        label = ttk.Label(self.first_screen, text="Welcome to Catan!", font=("Arial", 16))
        label.pack(pady=20)
        start_button = ttk.Button(self.first_screen, text="Start Game", command=self.get_player_count)
        start_button.pack(pady=10)
        
        self.player_count_widget = ttk.Entry(self.first_screen)
        self.player_count_widget.pack(pady=10)
        
        self.root.wait_window(self.first_screen)
        self.root.deiconify()  
        return self.player_count # Default to 3 players if none selected

    def get_player_count(self) -> int:
        try:
            count = int(self.player_count_widget.get())
            if count in [3, 4]:
                self.first_screen.destroy()
                self.player_count  = count
                return self.player_count
            else:
                raise ValueError
        except ValueError:
                pass
        return 3
    
    def place_initial_settlements(self, players: list):
        for player in players:
            self.game_struct.place_settlement_initial(player, self.board)
        for player in reversed(players):
            self.game_struct.place_settlement_initial(player, self.board)
        return
    
    def game_turn(self, players: list, update_player_stats_tab=None):
        first_die = random.randint(1, 6)
        second_die = random.randint(1, 6)
        self.first_dice.config(text=f"First Dice Roll: {first_die}")
        self.second_dice.config(text=f"Second Dice Roll: {second_die}")
        total = first_die + second_die
        self.total_of_dice.config(text=f"Total of Dice: {total}")

        if total != 7:
            self.game_struct.distribute_resources(total, players)
        
        # Update UI after resources are distributed
        if update_player_stats_tab:
            update_player_stats_tab()
        self.board.canvas.update()
       

        

        