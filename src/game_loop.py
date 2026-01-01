from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from game_struct import GameStruct
from canvas import Canvas


class GameLoop:
    
    def __init__(self, root: tk.Tk, game_struct: GameStruct, board: Canvas):
        
        self.root = root
        self.game_struct = game_struct
        self.board = board
        self.player_count = 3

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
        pass