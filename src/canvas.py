from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
import math

class Canvas:

    def __init__(self, root: ttk.Frame):
        self.root = root
        self.canvas = tk.Canvas(self.root, height=650, width=650)
        self.canvas.pack(expand=True, fill="both", anchor="center")
        self.__draw_hexagon(325,325, 50)

    def __draw_hexagon(self,x:int, y:int, size:float | int):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            px = x + size * math.cos(angle_rad)
            py = y + size * math.sin(angle_rad)
            points.extend([px, py])
        self.canvas.create_polygon(points, outline='black', fill='', width=2)