from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk

class Canvas:

    def __init__(self, root: ThemedTk):
        self.root = root
        #                                       5*130      5*130
        self.canvas = tk.Canvas(self.root, height=650, width=650)
        self.canvas.pack()