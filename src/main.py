from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from tabs import Tabs
from canvas import Canvas

def main():
    root = ThemedTk(theme="breeze")
    
    board = Canvas(root)
    
    tab = Tabs(root)

    tabs = tab.tabs()

    dice_tab = tab.dice_tab(tabs)

    trade_tab = tab.trade_tab(tabs)

    biuld_tab = tab.biuld_tab(tabs)
    
    root.mainloop()

if __name__ == "__main__":
    main()