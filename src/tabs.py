from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk

class Tabs:

    def __init__(self, root:ThemedTk):
        self.root = root

    def tabs(self):
        tab = ttk.Notebook(self.root)
        tab.pack(expand=True, fill="both")
        return tab
    
    def dice_tab(self, notebook:ttk.Notebook):

        dice_tab = ttk.Frame(notebook)
        notebook.add(dice_tab, text="dice")

    def trade_tab(self, notebook:ttk.Notebook):

        trade_tab = ttk.Frame(notebook)
        notebook.add(trade_tab, text="trade")

    def biuld_tab(self, notebook:ttk.Notebook):
        biuld_tab = ttk.Frame(notebook)
        notebook.add(biuld_tab, text="biuld")