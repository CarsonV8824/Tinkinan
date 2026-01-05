from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
import random
from game_struct import GameStruct
from canvas import Canvas



class GameLoop:
    
    def __init__(self, root: tk.Tk, game_struct: GameStruct, board: Canvas):
        
        self.root = root
        self.game_struct = game_struct
        self.board:Canvas = board
        self.player_count = 3
        self.first_dice = None
        self.second_dice = None
        self.total_of_dice = None

        self.player_index = 0

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
    
    """TODO: Make the players choose where to place their initial settlements and roads. 
        Try to keep canvas methods out of game struct class.
        hide tabs untill initial placement is done."""

    def placing_initial_settlements(self, players: list, tabs: ttk.Notebook=None):
        
        tabs.pack_forget() # Hide tabs during initial placementl
        
        total_initial_placements = len(players) * 2
        current_placement = 0

        while current_placement < total_initial_placements:
            current_player = players[self.player_index]

            self.board.canvas.update()
            self.board.settlement_init(current_player)
            self.board.road_init(current_player)
            current_placement += 1
            self.player_index = (self.player_index + 1) % len(players)
            

        tabs.pack(expand=True, fill="both") # Show tabs after placement is done
    
    def game_turn(self, player_info:ttk.Label, players: list,  first_dice_label:ttk.Label=None, second_dice_label:ttk.Label=None, total_of_dice_label:ttk.Label=None, update_player_stats_tab=None):
        
        self.board.canvas.update()
        first_die = random.randint(1, 6)
        second_die = random.randint(1, 6)
        first_dice_label.config(text=f"First Dice Roll: {first_die}")
        second_dice_label.config(text=f"Second Dice Roll: {second_die}")
        total = first_die + second_die
        total_of_dice_label.config(text=f"Total of Dice: {total}")

        if total != 7:
            self.game_struct.distribute_resources(total, players)
        
        # Update UI after resources are distributed
        if update_player_stats_tab:
            update_player_stats_tab()
        self.board.canvas.update()

        self.player_index = (self.player_index + 1) % len(players)
        
        player_info.config(text=f"{players[self.player_index].name}'s Turn")

        
       

        

        