from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from tabs import Tabs
from canvas import Canvas
from game_struct import GameStruct
from db import Database

def load_data():
    try:
        db = Database()
        return db.get_data()
    except Exception as e:
        print (e)

def main():
    
    root = ThemedTk(theme="breeze")
    root.geometry("1200x800")
    
    
    #===Scrollbar======================================================================================

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
        
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
        
    frame = ttk.Frame(scrollable_frame)
    frame.pack()

    #=====================================================================================
    
    board = Canvas(frame)
    
    tab = Tabs(frame)

    tabs = tab.tabs()

    dice_tab = tab.dice_tab(tabs)

    trade_tab = tab.trade_tab(tabs)

    biuld_tab = tab.biuld_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()