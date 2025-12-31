from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from tabs import Tabs

def main():
    root = ThemedTk(theme="breeze")
    
    gui = Tabs(root)

    tabs = gui.tabs()

    dice_tab = gui.dice_tab(tabs)

    trade_tab = gui.trade_tab(tabs)

    biuld_tab = gui.biuld_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()